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

#import json

from qgis.core import QgsMessageLog, QgsProject, QgsVectorLayer, QgsJsonUtils, QgsField, QgsFields, QgsVectorFileWriter, QgsCoordinateTransformContext
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtCore import QCoreApplication, QSettings, QTranslator
from qgis.PyQt.QtWidgets import QDialog

from PyQt5.uic import loadUi
from PyQt5 import QtCore

from ...form.textfield import TextField
from ..dropdown import DropDown
from ..array_field import ArrayField
from ..boolean import Boolean

UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'array_default.ui'))


class ArrayView(QtWidgets.QWidget, UI_CLASS):
    inputChanged = QtCore.pyqtSignal(object)

    def __init__(self, interface, json, schema, attr):
        """Constructor."""

        QDialog.__init__(self, interface.mainWindow())

        self.setupUi(self)

        self.json = json

        self.show()

        self.fieldArray = []

        #if 'items' in schema:
        #    field = ArrayField(interface, self.json, schema['items'], attr)
        #    return
        
        items = schema['properties'].items()

        for attr, value in items:

            valueType = value['type']

            if 'enum' in value:
                field = DropDown(interface, self.json, value, attr)
            elif valueType == 'boolean':
                field = Boolean(interface, self.json, value, attr)
                #field.lfbInfoBox.connect(self.infoBoxClicked)
            else:
                field = TextField(interface, self.json, value, attr)

            self.lfbTabLayout.addWidget(field)
            field.inputChanged.connect(self.emitText)
            
            self.fieldArray.append(field)

    def setJson(self, newJson, setFields = True):

        self.json = newJson

        for field in self.fieldArray :
            field.setJson(self.json, setFields)

    def emitText(self):
        self.inputChanged.emit(self.json)