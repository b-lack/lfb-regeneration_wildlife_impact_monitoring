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
import datetime
import uuid


from qgis.core import QgsFeature, QgsExpressionContextUtils, QgsPointXY, QgsGeometry, QgsMessageLog, QgsProject, QgsVectorLayer, QgsSymbol, QgsRendererRange, QgsGraduatedSymbolRenderer, QgsMarkerSymbol, QgsJsonUtils, QgsMapLayer, QgsField, QgsFields, QgsVectorFileWriter, QgsCoordinateTransformContext
from qgis.PyQt import QtWidgets, uic, QtGui
from qgis.PyQt.QtCore import QDateTime, QVariant, QCoreApplication, QSettings, QTranslator
from PyQt5.QtGui import QColor

from qgis.PyQt.QtWidgets import QDialog, QTableWidgetItem

from PyQt5.uic import loadUi
from PyQt5 import QtCore

from .io_btn import IoBtn
from .draft_item import DraftItem


# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'draft_selection.ui'))


class DraftSelection(QtWidgets.QWidget, UI_CLASS):
    # https://forum.qt.io/topic/133959/example-of-calling-a-function-to-parent/6
    draftSelected = QtCore.pyqtSignal(object, int)
    folderSelected = QtCore.pyqtSignal(str)

    def __init__(self, interface, schema):
        """Constructor."""

        # super(LfbRegenerationWildlifeImpactDialog, self).__init__(parent)
        QDialog.__init__(self, interface.mainWindow())

        

        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        self.schema = schema

        self.LAYER_PREFIX = "LFB-Regeneration-Wildlife-Impact-Monitoring"
        self.LAYER_VERSION = "0.0.1"

        # QGIS interface
        self.iface = interface

        self.fields = QgsFields()
        #self.fields.append(QgsField("fid", QVariant.DateTime))
        self.fields.append(QgsField("id", QVariant.String))
        self.fields.append(QgsField("status", QVariant.Bool))
        self.fields.append(QgsField("geometry", QVariant.Map))
        
        self.fields.append(QgsField("created", QVariant.DateTime))
        self.fields.append(QgsField("modified", QVariant.DateTime))
        self.fields.append(QgsField("workflow", QVariant.Int))
        self.fields.append(QgsField("unterlosnr", QVariant.String))

        self.fields.append(QgsField("form", QVariant.String))
        
        self.currentFeatureId = None

        self.addIoButton()

        self.show()

    def update(self):
        self.ioBtn.update()

    def imported(self, path):
        self.readDrafts()
        self.readDone(True)

    def addIoButton(self):
        self.ioBtn = IoBtn(self.iface)
        self.ioBtn.imported.connect(self.imported)
        #exportButton.importSelected.connect(self.draft.importSelected)
        self.lfbIoWidget.addWidget(self.ioBtn)

    def addLists(self):
        columnCount = 2

        tableHeaders = ['Name', 'Unterlos']
        self.lfbDraftTableView.setColumnCount(columnCount)
        self.lfbDraftTableView.setHorizontalHeaderLabels(tableHeaders)
        self.lfbDraftTableView.horizontalHeader().setStretchLastSection(True)

        self.addListRows()

    def addListRows(self):
        properties = self.readLayer()

        self.lfbDraftTableView.clear()
        self.lfbDraftTableView.setRowCount(len(properties))

        for rowNr, id in enumerate(properties):
            idx = 0
            
            for columnNr, column in id.items():
                self.lfbDraftTableView.setItem(rowNr, idx, QTableWidgetItem(str(id[columnNr])))
                idx += 1

    def resetCurrentDraft(self, featureId):
        self.currentFeatureId = featureId

    def setupDraftLayer(self):
        """Check if private layer exists"""
        

        names = [layer for layer in QgsProject.instance().mapLayers().values()]

        for i in names:
            if QgsExpressionContextUtils.layerScope(i).variable('LFB-NAME') == self.LAYER_PREFIX :
                
                self.vl = i

                folder = os.path.dirname(self.vl.dataProvider().dataSourceUri())
                self.folderSelected.emit(str(folder))

                self.readDrafts(False)
                self.readDone(True)
                return

        # https://anitagraser.com/pyqgis-101-introduction-to-qgis-python-programming-for-non-programmers/pyqgis101-creating-editing-a-new-vector-layer/
        self.vl = QgsVectorLayer("Point", self.LAYER_PREFIX, "memory")
        QgsExpressionContextUtils.setLayerVariable(self.vl, 'LFB-NAME', self.LAYER_PREFIX)
        QgsExpressionContextUtils.setLayerVariable(self.vl, 'LFB-VERSION', self.LAYER_VERSION)

        #self.vl.setFlags(QgsMapLayer.Private)
        self.setupSymbols()
        pr = self.vl.dataProvider()

        # add fields
        pr.addAttributes(self.fields)
        self.vl.updateFields() # tell the vector layer to fetch changes from the provider

        QgsProject.instance().addMapLayer(self.vl)
    
        
    def setDraftPath(self, path):
        pathToBeSet = os.path.join(path, self.LAYER_PREFIX + '.gpkg')
        writer = QgsVectorFileWriter.writeAsVectorFormatV3(self.vl, pathToBeSet, QgsCoordinateTransformContext(), QgsVectorFileWriter.SaveVectorOptions())

        if writer[0] == QgsVectorFileWriter.NoError:
            self.vl.setDataSource(pathToBeSet, self.vl.name(), 'ogr')
            self.vl.triggerRepaint() 
        else:
            print("error")

    
    def listWidgetClicked(self, item):
        featureList = self.vl.getFeatures()
        for feat in featureList:
            
            if(feat.id() == item):
                json_object = json.loads(feat['form'])
                self.currentFeatureId = feat.id()
                self.draftSelected.emit(json_object, self.currentFeatureId)
                break
            
    def setupSymbols(self):
        """Setup symbols for the layer"""

        values = (
            ('Von FU heruntergeladen - offline bei FU', 4, 4, '#decc44'),
            ('Sps', 1, 5, '#e62323'),
            ('bearbeitet oder hochgeladen', 5, 6, '#729b6f'),
            ('kontrolle', 7, 8, '#f3a6b2'),
            ('wiederholungsaufnahme', 11, 12, '#b80808'),
            ('sonstige', 13, 100, '#1228d1')
        )
        # create a category for each item in values
        ranges = []
        for label, lower, upper, color in values:
            symbol = QgsSymbol.defaultSymbol(self.vl.geometryType())
            symbol.setColor(QColor(color))
            rng = QgsRendererRange(lower, upper, symbol, label)
            ranges.append(rng)

        # create the renderer and assign it to a layer
        expression = 'workflow' # field name
        renderer = QgsGraduatedSymbolRenderer(expression, ranges)
        self.vl.setRenderer(renderer)

        #self..mapCanvas().refresh() 

    def readLayer(self):
        """Read the layer and return the features"""
        featureList = self.vl.getFeatures()
        sorted_featureList = sorted(featureList, key=lambda x: x['modified'], reverse=True)

        properties = []

        for feature in sorted_featureList:
            properties.append(json.loads(feature['properties']))

        return properties

    def readDrafts(self, status = False):

        for i in reversed(range(self.lfbDraftList.count())):
            self.lfbDraftList.itemAt(i).widget().setParent(None)

        featureList = self.vl.getFeatures()
        
        sorted_featureList = sorted(featureList, key=lambda x: x['modified'], reverse=True)
        filtered = filter(lambda c: c['status'] == status, sorted_featureList)
        sorted_featureList = list(filtered)
        
        for feature in sorted_featureList:
            item = DraftItem(self.iface, feature, self.schema)
            item.featureSelected.connect(self.listWidgetClicked)
            item.removeFeature.connect(self.removeFeature)
            self.lfbDraftList.addWidget(item)

        self.ioBtn.setExportLength(len(sorted_featureList))

    def readDone(self, status = False):

        for i in reversed(range(self.lfbDoneList.count())):
            self.lfbDoneList.itemAt(i).widget().setParent(None)

        featureList = self.vl.getFeatures()
        
        sorted_featureList = sorted(featureList, key=lambda x: x['modified'], reverse=True)
        filtered = filter(lambda c: c['status'] == status, sorted_featureList)
        sorted_featureList = list(filtered)
        
        for feature in sorted_featureList:
            item = DraftItem(self.iface, feature, self.schema)
            item.featureSelected.connect(self.listWidgetClicked)
            item.removeFeature.connect(self.removeFeature)
            self.lfbDoneList.addWidget(item)

    def removeFeature(self, featureId):
        self.vl.startEditing()
        self.vl.deleteFeature(featureId)
        self.vl.commitChanges()
        self.vl.endEditCommand()
        QgsProject.instance().write()
        self.readDrafts(False)
        self.readDone(True)
    
    def setStatus(self, newState):
        if self.currentFeatureId is not None:
            for tFeature in self.vl.getFeatures():
                if tFeature.id() == self.currentFeatureId:
                    self.vl.startEditing()
                    tFeature.setAttribute('status', newState)
                    self.vl.updateFeature(tFeature)
                    self.vl.commitChanges()
                    self.vl.endEditCommand()

    def saveFeature(self, jsonObj):

        if jsonObj is None:
            return
        
        if jsonObj['properties']['geometry']['coordinates'] is None:
            return 
        
        x = jsonObj['properties']['geometry']['coordinates'][0]
        y = jsonObj['properties']['geometry']['coordinates'][1]

        QgsMessageLog.logMessage(str(x) + ' ' + str(y), 'LFB')

        currentDateTime = QDateTime.currentDateTime()

        self.vl.startEditing()

        # check if feature exists
        if self.currentFeatureId is not None:

            for tFeature in self.vl.getFeatures():

                if tFeature.id() == self.currentFeatureId:
                    
                    tFeature.setAttribute('modified', currentDateTime)
                    feature = tFeature
                    geometry = QgsGeometry.fromPointXY(QgsPointXY(x, y))
                    feature.setGeometry(geometry)
        else:

            feature = QgsFeature()

            # inform the feature of its fields
            feature.setFields(self.vl.fields())

            geometry = QgsGeometry.fromPointXY(QgsPointXY(x, y))
            feature.setGeometry(geometry)

            #for attr, value in jsonObj.items():
            #    feature.setAttribute(attr, value)
            
            feature.setAttribute('id', str(uuid.uuid4()))
            feature.setAttribute('created', currentDateTime)
            feature.setAttribute('modified', currentDateTime)
            feature.setAttribute('status', 0)
            
            self.vl.addFeature(feature)
                
        # SET META DATA
        feature.setAttribute('workflow', jsonObj['general']['workflow'])
        feature.setAttribute('form', json.dumps(jsonObj))

        self.vl.updateFeature(feature)

        self.vl.commitChanges()
        self.vl.endEditCommand()
        QgsProject.instance().write()
        self.vl.updateExtents()

        for feature in self.vl.getFeatures():
            if feature['modified'] == currentDateTime:
                self.currentFeatureId = feature.id()

        self.readDrafts(False)
        self.readDone(True)
        #self.addListRows()


        



