# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gerrit/Sites/lfb/lfb-regeneration_wildlife_impact_monitoring/lfb_regeneration_wildlife_impact/gui/draft/draft_item.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_lfbItem(object):
    def setupUi(self, lfbItem):
        lfbItem.setObjectName("lfbItem")
        lfbItem.resize(940, 429)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(lfbItem.sizePolicy().hasHeightForWidth())
        lfbItem.setSizePolicy(sizePolicy)
        lfbItem.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(lfbItem)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lfbItemFrame = QtWidgets.QFrame(lfbItem)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfbItemFrame.sizePolicy().hasHeightForWidth())
        self.lfbItemFrame.setSizePolicy(sizePolicy)
        self.lfbItemFrame.setObjectName("lfbItemFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.lfbItemFrame)
        self.verticalLayout_2.setContentsMargins(20, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, -1, 0, -1)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.lfbItemFrame)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lfbDraftModifiedByBtn = QtWidgets.QLabel(self.lfbItemFrame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lfbDraftModifiedByBtn.setFont(font)
        self.lfbDraftModifiedByBtn.setObjectName("lfbDraftModifiedByBtn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lfbDraftModifiedByBtn)
        self.label_4 = QtWidgets.QLabel(self.lfbItemFrame)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lfbDraftModifiedBtn = QtWidgets.QLabel(self.lfbItemFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfbDraftModifiedBtn.sizePolicy().hasHeightForWidth())
        self.lfbDraftModifiedBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lfbDraftModifiedBtn.setFont(font)
        self.lfbDraftModifiedBtn.setObjectName("lfbDraftModifiedBtn")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lfbDraftModifiedBtn)
        self.label_2 = QtWidgets.QLabel(self.lfbItemFrame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lfbDraftAufnahmetruppLabel = QtWidgets.QLabel(self.lfbItemFrame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lfbDraftAufnahmetruppLabel.setFont(font)
        self.lfbDraftAufnahmetruppLabel.setObjectName("lfbDraftAufnahmetruppLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lfbDraftAufnahmetruppLabel)
        self.horizontalLayout_5.addLayout(self.formLayout)
        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lfbDraftIconRemoveBtn = QtWidgets.QToolButton(self.lfbItemFrame)
        self.lfbDraftIconRemoveBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lfbDraftIconRemoveBtn.setStyleSheet("color: red;\n"
"padding:10px 0;\n"
"border: none;\n"
"border-radius: 5px;")
        self.lfbDraftIconRemoveBtn.setObjectName("lfbDraftIconRemoveBtn")
        self.horizontalLayout_2.addWidget(self.lfbDraftIconRemoveBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lfbFocusBtn = QtWidgets.QPushButton(self.lfbItemFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfbFocusBtn.sizePolicy().hasHeightForWidth())
        self.lfbFocusBtn.setSizePolicy(sizePolicy)
        self.lfbFocusBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lfbFocusBtn.setStyleSheet("background-color: green;\n"
"padding:5px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: white;")
        self.lfbFocusBtn.setObjectName("lfbFocusBtn")
        self.horizontalLayout_2.addWidget(self.lfbFocusBtn)
        self.lfbDraftIconBtn = QtWidgets.QPushButton(self.lfbItemFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfbDraftIconBtn.sizePolicy().hasHeightForWidth())
        self.lfbDraftIconBtn.setSizePolicy(sizePolicy)
        self.lfbDraftIconBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lfbDraftIconBtn.setStyleSheet("background-color: green;\n"
"padding:10px;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: white;")
        self.lfbDraftIconBtn.setObjectName("lfbDraftIconBtn")
        self.horizontalLayout_2.addWidget(self.lfbDraftIconBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addWidget(self.lfbItemFrame, 0, 0, 1, 1)

        self.retranslateUi(lfbItem)
        QtCore.QMetaObject.connectSlotsByName(lfbItem)

    def retranslateUi(self, lfbItem):
        _translate = QtCore.QCoreApplication.translate
        lfbItem.setWindowTitle(_translate("lfbItem", "Form"))
        self.label.setText(_translate("lfbItem", "Modified:"))
        self.lfbDraftModifiedByBtn.setText(_translate("lfbItem", "-"))
        self.label_4.setText(_translate("lfbItem", "Created:"))
        self.lfbDraftModifiedBtn.setText(_translate("lfbItem", "-"))
        self.label_2.setText(_translate("lfbItem", "Aufnahmetrupp:"))
        self.lfbDraftAufnahmetruppLabel.setText(_translate("lfbItem", "-"))
        self.lfbDraftIconRemoveBtn.setText(_translate("lfbItem", "löschen"))
        self.lfbFocusBtn.setText(_translate("lfbItem", "Fokus"))
        self.lfbDraftIconBtn.setText(_translate("lfbItem", "AUSWÄHLEN"))
