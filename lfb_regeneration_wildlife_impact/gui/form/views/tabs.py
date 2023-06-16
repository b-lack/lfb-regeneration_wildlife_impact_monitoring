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
from qgis.PyQt.QtWidgets import QDialog

from PyQt5 import QtCore

from ...form.textfield import TextField
from ..textarea import TextArea
from ..dropdown import DropDown
from ..array_field import ArrayField
from ..boolean import Boolean

UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'tab_default.ui'))


class Tabs(QtWidgets.QWidget, UI_CLASS):
    inputChanged = QtCore.pyqtSignal(object)

    def __init__(self, interface, json, schema):
        """Constructor."""

        QDialog.__init__(self, interface.mainWindow())

        self.setupUi(self)

        self.json = json

        self.show()

        self.infoTitle = ""

        self.fieldArray = []

        #if 'title' in schema:
        #    self.lfbObjectHeadeline.setText(schema['title'])
        #else:
        #    self.lfbObjectHeadeline.hide()

        if 'description' in schema:
            self.lfbObjectDescription.setText(schema['description'])
        else:
            self.lfbObjectDescription.hide()

        if 'properties' in schema:
            items = schema['properties'].items()
        else:
            items = schema['items'].items()

        for attr, value in items:
            
            valueType = value['type']

            if valueType == 'array':
                field = ArrayField(interface, self.json, value, attr)
            elif valueType == 'boolean':
                field = Boolean(interface, self.json, value, attr)
                field.lfbInfoBox.connect(self.infoBoxClicked)
            elif 'enum' in value:
                field = DropDown(interface, self.json, value, attr)
                field.lfbInfoBox.connect(self.infoBoxClicked)
            elif 'maxLength' in value and value['maxLength'] >= 1000:
                field = TextArea(interface, self.json, value, attr)
                field.lfbInfoBox.connect(self.infoBoxClicked)
            else:
                field = TextField(interface, self.json, value, attr)
                field.lfbInfoBox.connect(self.infoBoxClicked)
                
            self.lfbTabLayout.addWidget(field)
            field.inputChanged.connect(self.emitText)

            self.fieldArray.append(field)

        self.lfbInfoBox.hide()

    def infoBoxClicked(self, info):

        if self.infoTitle == info['title']:
            if self.lfbInfoBox.isVisible():
                self.lfbInfoBox.hide()
            else:
                self.lfbInfoBox.show()
        else:
            self.lfbInfoBox.setText(info['description'])
            self.lfbInfoBox.show()

        self.infoTitle = info['title']


    def setJson(self, newJson, setFields = True):
        
        self.json = newJson

        for field in self.fieldArray :
            field.setJson(self.json, setFields)

    def emitText(self):
        self.inputChanged.emit(self.json)