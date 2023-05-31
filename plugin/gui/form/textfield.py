# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LfbRegenerationWildlifeImpactDialog
                                 A QGIS plugin
 Lfb Regeneration and Wildlife Impact Monitoring
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-05-08
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Grünecho
        email                : support@grunecho.de
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

import json

from qgis.core import QgsMessageLog, QgsProject, QgsVectorLayer, QgsJsonUtils, QgsField, QgsFields, QgsVectorFileWriter, QgsCoordinateTransformContext
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtCore import QCoreApplication, QSettings, QTranslator
from qgis.PyQt.QtWidgets import QDialog

from PyQt5.uic import loadUi
from PyQt5 import QtCore

from jsonschema import Draft7Validator


UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'textfield.ui'))


class TextField(QtWidgets.QWidget, UI_CLASS):
    inputChanged = QtCore.pyqtSignal(str)

    def __init__(self, interface, json, schema, key):
        """Constructor."""

        QDialog.__init__(self, interface.mainWindow())

        self.setupUi(self)

        if(key not in json):
            json[key] = None

        self.json = json
        self.internJson = json.copy()
        self.schema = schema
        self.key = key
        self.defaultValue = self.json[self.key]

        #self.lfbTextFieldSuccess.hide()
        #self.lfbTextFieldError.hide()


        self.lfbTextFieldLabel.setText(self.schema['properties'][self.key]['title'])
        self.lfbTextField.textChanged.connect(self.setInputText)
        self.lfbTextField.undoAvailable = True

        self.validate() 

        self.show()

    def setJson(self, newJson):
        self.json = newJson
        
        if self.json is not None and self.json[self.key] is not None:
            self.lfbTextField.setText(str(self.json[self.key]))
        else:
            self.lfbTextField.setText("")

        
        
    def isfloat(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False
    def setInputText(self, text):
        valueStr = self.lfbTextField.text()

        if valueStr is "":
            value = None

        elif self.schema['properties'][self.key]['type'] == "number" and self.isfloat(valueStr):
            value = float(valueStr)
            
        elif self.schema['properties'][self.key]['type'] == "integer" and valueStr.isnumeric():
            value = int(valueStr)
        else:
            value = valueStr

        self.internJson[self.key] = value


        self.validate()

    def validate(self):
        #jsonCpy = self.json.copy()
        #jsonCpy['name'] = self.lfbTextField.text()

        # https://python-jsonschema.readthedocs.io/en/stable/validate/
        v = Draft7Validator(self.schema['properties'][self.key])
        errors = sorted(v.iter_errors(self.internJson[self.key]), key=lambda e: e.path)

        self.json[self.key] = self.internJson[self.key]

        if len(errors) == 0:
            self.lfbTextFieldError.hide()
            self.lfbTextFieldSuccess.show()
            #self.emitText()
        else:
            self.lfbTextFieldError.show()
            self.lfbTextFieldSuccess.hide()
            for error in errors:
                self.lfbTextFieldError.setText(error.message)

        self.inputChanged.emit(str(self.json[self.key]))