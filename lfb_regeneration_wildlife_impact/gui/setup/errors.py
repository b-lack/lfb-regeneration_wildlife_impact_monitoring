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

from qgis.core import QgsMessageLog, QgsProject
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtWidgets import QDialog

from PyQt5.uic import loadUi
from PyQt5 import QtCore

UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'errors.ui'))

class ErrorsWidget(QtWidgets.QWidget, UI_CLASS):

    def __init__(self, interface, schema):
        """Constructor."""

        QDialog.__init__(self, interface.mainWindow())

        self.setupUi(self)

        self.iface = interface
        self.errors = []
        self.schema = schema

        self.show()


    def findNameInJsonSchema(self, name, schema):
        for key, value in schema.items():
            if key == name:
                return value
            elif isinstance(value, dict):
                return self.findNameInJsonSchema(name, value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        return self.findNameInJsonSchema(name, item)
        return None
    
    def translateRelativeSchemaPath(self, relative_schema_path):
        # QgsMessageLog.logMessage(str(relative_schema_path), 'LFB')
        isProperties = False
        tab = None
        tabCount = None

        for path in relative_schema_path:

            if isProperties and not tab:
                tabCount = 0
                for key, value in self.schema['properties'].items():
                    if path  == key:
                        tab = self.schema['properties'][path]
                        break
                    tabCount += 1

            if path == 'properties':
                isProperties = True
            
           
        if tab is not None and 'title' in tab:
            return tab['title']
        
        return ''
    
    def updateErrors(self, errors):
        self.errors = errors

        self.lfbErrorsOfCount.hide()
        self.lfbErrorsOfCount.setText(str(len(self.errors)))

        

        if len(self.errors) > 0:
            errorLocation = self.translateRelativeSchemaPath(self.errors[0].relative_schema_path)
            self.lfbErrorLocation.setText(errorLocation)
            self.lfbErrorDescription.setText(str(self.errors[0].message))
            self.show()
        else:
            self.lfbErrorLocation.setText('')
            self.lfbErrorDescription.setText('')
            self.hide()
