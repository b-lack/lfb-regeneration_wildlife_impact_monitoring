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

from qgis.core import QgsMessageLog
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtCore import QCoreApplication
from qgis.PyQt.QtWidgets import QDialog, QPushButton

from PyQt5.uic import loadUi
from PyQt5 import QtCore

from jsonschema import Draft7Validator

from ...utils.helper import Utils
from .chips import Chips

UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'dropdown.ui'))


class DropDown(QtWidgets.QWidget, UI_CLASS):
    inputChanged = QtCore.pyqtSignal(object, str)
    lfbInfoBox = QtCore.pyqtSignal(object)

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

        

        self.lfbTextFieldLabel.setText(QCoreApplication.translate("FormFields", self.schema['title']))
        
        self.lfbTextFieldHelp.setText('')
        if "description" in self.schema:
            self.lfbTextFieldHelp.setText(self.schema['description'])
        else:
            self.lfbTextFieldHelp.hide()

        if "readOnly" in self.schema:
            self.lfbComboBox.setEnabled(not self.schema['readOnly'])

        if "unit" in self.schema:
            self.lfbUnit.setText(self.schema['unit'])

        if "helpText" in self.schema:
            self.lfbTextFieldDescriptionBtn.show()
        else:
            self.lfbTextFieldDescriptionBtn.hide()

        self.lfbComboBox.currentIndexChanged.connect(self.setInputText)
        self.lfbComboBox.addItems(self.schema['enumLabels'])

        self.lfbTextFieldDescriptionBtn.clicked.connect(self.triggerInfoBox)

        
        if "QTType" in self.schema and self.schema['QTType'] == "tree":
            #self.lfbReplaceWidget.show()
            #self.lfbComboBox.hide()
            self.lfbComboBox.setEnabled(False)
            
            self.tree = QtWidgets.QTreeWidget()
            self.tree.setFixedHeight(300)
            self.tree.setStyleSheet("QTreeWidget { font-size: 13pt; }")
            self.tree.itemClicked.connect(self.onItemClicked)
            self.lfbReplaceWidget.layout().addWidget(self.tree)

            self.createTreeWidget(self.schema)


        if "default" in self.schema and self.json[self.key] is None:
            self.setDefaultValue()
            

        if "qtChips" in self.schema:
            self.chips = Chips(interface, self.schema, self.schema['qtChips'])
            self.chips.inputChanged.connect(self.setIndex)
            self.lfbChipsLayout.addWidget(self.chips)
            index = self.schema['enum'].index(self.json[self.key])
            self.chips.setValue(self.schema['enumLabels'][index])


        if "writeOnly" in self.schema:
            if self.schema['writeOnly'] == True:
                self.lfbComboBox.hide()
            else:
                self.lfbComboBox.show()

        self.validate(True) 
        
    def setDefaultValue(self):
        if "default" not in self.schema:
            self.internJson[self.key] = None
            self.lfbComboBox.setCurrentIndex(0)
            return
        
        index = self.schema['enum'].index(self.schema['default'])

        if index == -1:
            return
        
        
        self.internJson[self.key] = self.schema['default']
        self.lfbComboBox.setCurrentIndex(index)

        
        
    def triggerInfoBox(self):
        self.lfbInfoBox.emit(self.schema)

    def setJson(self, newJson, setFields = True):

        self.json = newJson

        if self.key not in newJson:
            QgsMessageLog.logMessage("Key not in Json: " + self.key, 'LFG')
            self.setDefaultValue()
            # self.json[self.key] = None
        else:
            self.json[self.key] = newJson[self.key]

        if setFields == False:
            return

        if self.key not in self.json:
            return
            #self.json[self.key] = None

        

        if self.json is not None and self.json[self.key] is not None:
            vType = type(self.json[self.key])
            
            index = self.schema['enum'].index(int(self.json[self.key]))

            if index != -1:
                self.lfbComboBox.setCurrentIndex(index)
        else:
            self.setDefaultValue()

            # self.lfbComboBox.setCurrentIndex(0)

        if "QTType" in self.schema and self.schema['QTType'] == "tree":
            self.createTreeWidget(self.schema)

        
        
    def isfloat(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False
        
    #from Chips
    def setIndex(self, value):

        self.setInputText(value, False)
        if value is not None and self.lfbComboBox.currentIndex() != value:
            self.lfbComboBox.setCurrentIndex(value)

    #from dd
    def setInputText(self, value, setChips = True):
        
        value = self.schema['enum'][value]

        if setChips and hasattr(self, 'chips'):
            index = self.schema['enum'].index(value)
            self.chips.setValue(self.schema['enumLabels'][index])

        self.internJson[self.key] = value

        self.validate(True)

        #self.lfbTextFieldHelp.show()
        #self.lfbTextFieldHelp.setText(str(self.internJson[self.key]))
        
    def validate(self, emit = False):

        # https://python-jsonschema.readthedocs.io/en/stable/validate/
        v = Draft7Validator(self.schema)
        errors = sorted(v.iter_errors(self.internJson[self.key]), key=lambda e: e.path)

        self.json[self.key] = self.internJson[self.key]

        #if self.json[self.key] is None:
        #    self.lfbTextFieldError.hide()
        #    self.lfbTextFieldSuccess.hide()
        #    self.lfbTextFieldHelp.show()

        if len(errors) == 0:
            self.lfbTextFieldError.hide()
            self.lfbTextFieldSuccess.hide()
            self.lfbTextFieldHelp.show()
            self.lfbComboBox.setStyleSheet("QComboBox {\n	border: 2px solid green;\n	border-radius: 10px;\n	padding: 10px;\n}")

            #if "QTType" in self.schema and self.schema['QTType'] == "tree":
                #self.lfbTextFieldLabel.setText(Utils.enumLabel(self.json[self.key], self.schema))
                #self.lfbTextFieldLabel.setText(QCoreApplication.translate("FormFields", Utils.enumLabel(self.json[self.key], self.schema)))
        else:
            self.lfbTextFieldError.show()
            self.lfbTextFieldSuccess.hide()
            self.lfbTextFieldHelp.hide()
            self.lfbComboBox.setStyleSheet("QComboBox {\n	border: 2px solid red;\n	border-radius: 10px;\n	padding: 10px;\n}")

            for error in errors:
                if "is not type":
                    self.lfbTextFieldError.setText(QCoreApplication.translate("errorMessages", 'Eine Auswahl ist pflicht.'))
                else:
                    self.lfbTextFieldError.setText(QCoreApplication.translate("errorMessages", error.message))
        if emit:
            self.inputChanged.emit(self.json[self.key], self.key)

    def setTreeItems(self, tree, items):

        for attr, item in items.items():

            child = QtWidgets.QTreeWidgetItem(tree)

            
            child.setText(0, item['name'])
            child.setData(0, 1, attr)

            child.setSelected(attr == str(self.json[self.key]))

            if 'children' in item:
                self.setTreeItems(child, item['children'])

    def onItemClicked(self, item, column):

        if str(item.data(column, 1)) == 'None':
            self.internJson[self.key] = 0
        else:
            self.internJson[self.key] = int(item.data(column, 1))

        self.validate()

        
        index = self.schema['enum'].index(self.json[self.key])
        if index != -1:
            self.lfbComboBox.setCurrentIndex(index)

    def createTreeWidget(self, data):
        
        self.tree.clear()

        self.tree.setHeaderLabels([self.schema['title']])

        items = {}

        for idx, item in enumerate(data['enum']):
            if item is None or item < 100 :
                items[str(item)] = {
                    'name': data['enumLabels'][idx],
                    'children': {}
                }

        for idx, item in enumerate(data['enum']):
            if item is not None and item > 100 :
                if item < 10000:
                    index = int(str(item)[0])
                else:
                    index = int(str(item)[0] + str(item)[1])

                if str(index) in items :
                    items[str(index)]['children'][str(item)] = {
                        'name': data['enumLabels'][idx],
                        'children': {}
                    }
                else:
                    items[str(item)] = {
                        'name': data['enumLabels'][idx],
                        'children': {}
                    }

        self.setTreeItems(self.tree, items)