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

from qgis.core import QgsFeature, QgsMessageLog, QgsProject, QgsVectorLayer, QgsMapLayer
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtCore import QCoreApplication, QSettings, QTranslator
from qgis.PyQt.QtWidgets import QDialog

from PyQt5.uic import loadUi

import json
import copy

from .form.textfield import TextField

from .form.views.tab1 import Tab1
from .form.views.tab2 import Tab2
from .form.views.tab3 import Tab3

from .draft.draft_selection import DraftSelection
from .setup.folder_selection import FolderSelection

from .form.saveBar import SaveBar

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'lfb_regeneration_wildlife_impact_dialog_base.ui'))


class LfbRegenerationWildlifeImpactDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, interface, state):
        """Constructor.

        :type state: CurrentState
        """

        # super(LfbRegenerationWildlifeImpactDialog, self).__init__(parent)
        QDialog.__init__(self, interface.mainWindow())

        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        # QGIS interface
        self.iface = interface

        self.json = {
            "aufnahmetrupp": None,
            "GNSSDevice": None,
            "coordinates": {
                "latitude": None,
                "longitude": None,
            },
            "stichprobenpunkt": {
                "unbestockt": None,
                "nichtWald": None
            }
        }
        self.defaultJson = {
            "aufnahmetrupp": None,
            "GNSSDevice": None,
            "coordinates": {
                "latitude": None,
                "longitude": None,
            },
            "stichprobenpunkt": {
                "unbestockt": None,
                "nichtWald": None
            }
        }

        self.state = state

        # Connect up the buttons.
        self.lfbHomeBtn.clicked.connect(self.openHome)
        self.lfbQuestionBtn.clicked.connect(self.openQuestionDialog)

        self.lfbDevBtn.clicked.connect(self.openState)
        
        self.addFolderSelection()
        self.addDraft()

        dirname = os.path.dirname(__file__)
        filename = os.path.realpath(os.path.join(dirname, '..', 'schema', 'vwm.json'))

        with open(filename) as f:
            self.schema = json.load(f)
        

        self.lfbNewEntry.clicked.connect(self.newEntry)

      
        self.tab1 = Tab1(self.iface, self.json, self.schema)
        self.tab1.inputChanged.connect(self.inputChanged)
        self.lfbTab1Layout.addWidget(self.tab1)

        self.tab2 = Tab2(self.iface, self.json, self.schema)
        self.tab2.inputChanged.connect(self.inputChanged)
        self.lfbTab2Layout.addWidget(self.tab2)

        self.tab3 = Tab3(self.iface, self.json, self.schema)
        self.tab3.inputChanged.connect(self.inputChanged)
        self.lfbTab3Layout.addWidget(self.tab3)

        self.saveBar = SaveBar(self.iface, self.json, self.schema)
        self.verticalLayout_4.addWidget(self.saveBar)

        self.resetForm()
        self.setPosition(1)

    def resetForm(self):
        self.tab1.setJson(self.json)
        self.tab2.setJson(self.json)
        self.tab3.setJson(self.json)
        QgsMessageLog.logMessage(str(self.defaultJson), "LFB")

    def newEntry(self):
        self.json = copy.deepcopy(self.defaultJson)
        self.changeState()
        self.setPosition(2)

    def inputChanged(self, save):
        self.changeState()
        
        if self.saveBar.validate(self.json) == True:
            self.draft.saveFeature(self.json)

    def openHome(self):
        self.json = copy.deepcopy(self.defaultJson)
        self.changeState()
        QgsMessageLog.logMessage(str(self.defaultJson), "LFB")
        self.setPosition(1)

    def setPosition(self, position):

        self.userPosition = position

        if self.userPosition == 2:
            self.lfbNewEntry.hide()
            self.tabWidget.show()
            self.saveBar.show()
            self.draft.hide()
            self.folderSelection.hide()
            self.lfbHomeBtn.setEnabled(True)
        elif self.userPosition == 3:
            self.lfbNewEntry.hide()
            self.tabWidget.show()
            self.saveBar.show()
            self.draft.hide()
            self.folderSelection.hide()
            self.lfbHomeBtn.setEnabled(True)
        else: 
            self.lfbNewEntry.show()
            self.tabWidget.hide()
            self.saveBar.hide()
            self.draft.show()
            self.folderSelection.show()
            self.lfbHomeBtn.setEnabled(False)

    def addFolderSelection(self):
        self.folderSelection = FolderSelection(self.iface)
        self.folderSelection.folderSelected.connect(self.folderSelected)
        self.verticalLayout_4.addWidget(self.folderSelection)
        

    def folderSelected(self, folderPath):
        self.draftPath = folderPath
        self.draft.setDraftPath(folderPath)

    def addDraft(self):
        self.draft = DraftSelection(self.iface)
        self.draft.draftSelected.connect(self.draftSelected)
        self.verticalLayout_4.addWidget(self.draft)

    def draftSelected(self, id):
        self.json = id
        self.resetForm()
        self.changeState()
        self.setPosition(2)

    def changeState(self):
        self.state.change_state(self.json)
        self.saveBar.validate(self.state.state)
        self.resetForm()

    def openState(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(json.dumps(self.state.state, indent=2))
        msgBox.exec()

    def openQuestionDialog(self):
        msg = self.tr('Infotext')

        QtWidgets.QMessageBox.information(
            self, "LFB Info", msg, QtWidgets.QMessageBox.Ok)
