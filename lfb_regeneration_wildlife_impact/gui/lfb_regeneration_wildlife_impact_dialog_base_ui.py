# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gerrit/Sites/lfb/lfb-regeneration_wildlife_impact_monitoring/lfb_regeneration_wildlife_impact/gui/lfb_regeneration_wildlife_impact_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LfbRegenerationWildlifeImpactDialogBase(object):
    def setupUi(self, LfbRegenerationWildlifeImpactDialogBase):
        LfbRegenerationWildlifeImpactDialogBase.setObjectName("LfbRegenerationWildlifeImpactDialogBase")
        LfbRegenerationWildlifeImpactDialogBase.resize(921, 645)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LfbRegenerationWildlifeImpactDialogBase.sizePolicy().hasHeightForWidth())
        LfbRegenerationWildlifeImpactDialogBase.setSizePolicy(sizePolicy)
        LfbRegenerationWildlifeImpactDialogBase.setMinimumSize(QtCore.QSize(400, 100))
        self.gridLayout = QtWidgets.QGridLayout(LfbRegenerationWildlifeImpactDialogBase)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.lfbTabWidget = QtWidgets.QTabWidget(LfbRegenerationWildlifeImpactDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.lfbTabWidget.sizePolicy().hasHeightForWidth())
        self.lfbTabWidget.setSizePolicy(sizePolicy)
        self.lfbTabWidget.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lfbTabWidget.setFont(font)
        self.lfbTabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lfbTabWidget.setStyleSheet("QTabBar{\n"
"    alignment: center;\n"
"    background-color: #222;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"    border: none;\n"
"    qproperty-drawBase: 0;\n"
"    border-top: 0px;\n"
"}\n"
"QTabBar::tab {\n"
"    background-color: transparent;\n"
"    width: 32px;\n"
"    height: 32px;\n"
"    margin: 10px 10px 0 10px;\n"
"    border-radius: 10px;\n"
"    padding: 0px;\n"
"    text-align: center;\n"
"}\n"
"QTabBar::tab:enabled{\n"
"    background-color: transparent;\n"
"}\n"
"QTabBar::tab:selected{\n"
"    color: black;\n"
"    height: 32px;\n"
"    margin:  7px 7px 0px 7px;\n"
"    padding: 0px 5px 10px 5px;\n"
"    border: none;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    background-color: #eee;\n"
"}\n"
"QTabWidget::pane { border: 0; }")
        self.lfbTabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.lfbTabWidget.setIconSize(QtCore.QSize(32, 32))
        self.lfbTabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.lfbTabWidget.setDocumentMode(True)
        self.lfbTabWidget.setMovable(False)
        self.lfbTabWidget.setObjectName("lfbTabWidget")
        self.gridLayout.addWidget(self.lfbTabWidget, 2, 0, 1, 1)
        self.lfbHomeScreen = QtWidgets.QScrollArea(LfbRegenerationWildlifeImpactDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.lfbHomeScreen.sizePolicy().hasHeightForWidth())
        self.lfbHomeScreen.setSizePolicy(sizePolicy)
        self.lfbHomeScreen.setStyleSheet("margin:0;\n"
"padding:0;")
        self.lfbHomeScreen.setWidgetResizable(True)
        self.lfbHomeScreen.setObjectName("lfbHomeScreen")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 919, 319))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lfbHeadline = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfbHeadline.sizePolicy().hasHeightForWidth())
        self.lfbHeadline.setSizePolicy(sizePolicy)
        self.lfbHeadline.setObjectName("lfbHeadline")
        self._2 = QtWidgets.QVBoxLayout(self.lfbHeadline)
        self._2.setContentsMargins(-1, 50, -1, 10)
        self._2.setObjectName("_2")
        self.label = QtWidgets.QLabel(self.lfbHeadline)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self._2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.lfbHeadline)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self._2.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 20, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lfbNewEntry = QtWidgets.QPushButton(self.lfbHeadline)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lfbNewEntry.setFont(font)
        self.lfbNewEntry.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lfbNewEntry.setStyleSheet("QPushButton{\n"
"    border-radius: 20px;\n"
"    border: 2px solid #333;\n"
"    color: #555;\n"
"    margin: 10px 0px 0px;\n"
"    padding: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: yellow;\n"
"}\n"
"QPushButton:enabled{\n"
"    border-radius: 20px;\n"
"    border: 2px solid #fff;\n"
"    background-color: green;\n"
"    color: #fff;\n"
"}")
        self.lfbNewEntry.setObjectName("lfbNewEntry")
        self.horizontalLayout.addWidget(self.lfbNewEntry)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self._2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.lfbHeadline)
        self.lfbHomeInputs = QtWidgets.QVBoxLayout()
        self.lfbHomeInputs.setSpacing(0)
        self.lfbHomeInputs.setObjectName("lfbHomeInputs")
        self.verticalLayout.addLayout(self.lfbHomeInputs)
        self.lfbHomeScreen.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.lfbHomeScreen, 3, 0, 1, 1)
        self.lfbMain = QtWidgets.QVBoxLayout()
        self.lfbMain.setContentsMargins(-1, 0, -1, -1)
        self.lfbMain.setSpacing(0)
        self.lfbMain.setObjectName("lfbMain")
        self.gridLayout.addLayout(self.lfbMain, 1, 0, 1, 1)

        self.retranslateUi(LfbRegenerationWildlifeImpactDialogBase)
        self.lfbTabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(LfbRegenerationWildlifeImpactDialogBase)

    def retranslateUi(self, LfbRegenerationWildlifeImpactDialogBase):
        _translate = QtCore.QCoreApplication.translate
        LfbRegenerationWildlifeImpactDialogBase.setWindowTitle(_translate("LfbRegenerationWildlifeImpactDialogBase", "Lfb Regeneration and Wildlife Impact Monitoring"))
        self.label.setText(_translate("LfbRegenerationWildlifeImpactDialogBase", "Verbiss und Wildtier Monitoring w"))
        self.label_2.setText(_translate("LfbRegenerationWildlifeImpactDialogBase", "Überwachung des Verjüngungszustandes durch die Aufnahme von Naturaldaten."))
        self.lfbNewEntry.setText(_translate("LfbRegenerationWildlifeImpactDialogBase", "AUFNAHME STARTEN"))
