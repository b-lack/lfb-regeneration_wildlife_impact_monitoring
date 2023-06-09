# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gerrit/Sites/lfb/lfb-regeneration_wildlife_impact_monitoring/lfb_regeneration_wildlife_impact/gui/form/dropdown.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(891, 404)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 10, 0, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.lfbTextFieldError = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfbTextFieldError.sizePolicy().hasHeightForWidth())
        self.lfbTextFieldError.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lfbTextFieldError.setFont(font)
        self.lfbTextFieldError.setStyleSheet("color: red;")
        self.lfbTextFieldError.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lfbTextFieldError.setObjectName("lfbTextFieldError")
        self.gridLayout.addWidget(self.lfbTextFieldError, 6, 1, 1, 1)
        self.lfbTextFieldDescriptionBtn = QtWidgets.QToolButton(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lfbTextFieldDescriptionBtn.setFont(font)
        self.lfbTextFieldDescriptionBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lfbTextFieldDescriptionBtn.setStyleSheet("QToolButton{\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    margin-right: 10px;\n"
"}")
        self.lfbTextFieldDescriptionBtn.setObjectName("lfbTextFieldDescriptionBtn")
        self.gridLayout.addWidget(self.lfbTextFieldDescriptionBtn, 3, 0, 1, 1)
        self.lfbComboBox = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfbComboBox.sizePolicy().hasHeightForWidth())
        self.lfbComboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lfbComboBox.setFont(font)
        self.lfbComboBox.setCursor(QtGui.QCursor(QtCore.Qt.SizeAllCursor))
        self.lfbComboBox.setStyleSheet("QComboBox {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}")
        self.lfbComboBox.setCurrentText("")
        self.lfbComboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.lfbComboBox.setObjectName("lfbComboBox")
        self.gridLayout.addWidget(self.lfbComboBox, 3, 1, 1, 1)
        self.lfbTextFieldHelp = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfbTextFieldHelp.sizePolicy().hasHeightForWidth())
        self.lfbTextFieldHelp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lfbTextFieldHelp.setFont(font)
        self.lfbTextFieldHelp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lfbTextFieldHelp.setWordWrap(True)
        self.lfbTextFieldHelp.setObjectName("lfbTextFieldHelp")
        self.gridLayout.addWidget(self.lfbTextFieldHelp, 5, 1, 1, 1)
        self.lfbUnit = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lfbUnit.setFont(font)
        self.lfbUnit.setText("")
        self.lfbUnit.setObjectName("lfbUnit")
        self.gridLayout.addWidget(self.lfbUnit, 3, 2, 1, 1)
        self.lfbReplaceWidget = QtWidgets.QGridLayout()
        self.lfbReplaceWidget.setSpacing(0)
        self.lfbReplaceWidget.setObjectName("lfbReplaceWidget")
        self.gridLayout.addLayout(self.lfbReplaceWidget, 4, 1, 1, 2)
        self.lfbTextFieldSuccess = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfbTextFieldSuccess.sizePolicy().hasHeightForWidth())
        self.lfbTextFieldSuccess.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lfbTextFieldSuccess.setFont(font)
        self.lfbTextFieldSuccess.setStyleSheet("color: green;")
        self.lfbTextFieldSuccess.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lfbTextFieldSuccess.setObjectName("lfbTextFieldSuccess")
        self.gridLayout.addWidget(self.lfbTextFieldSuccess, 7, 1, 1, 1)
        self.lfbTextFieldLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfbTextFieldLabel.sizePolicy().hasHeightForWidth())
        self.lfbTextFieldLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lfbTextFieldLabel.setFont(font)
        self.lfbTextFieldLabel.setObjectName("lfbTextFieldLabel")
        self.gridLayout.addWidget(self.lfbTextFieldLabel, 1, 1, 1, 1)
        self.horizontalWidget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.lfbChipsLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.lfbChipsLayout.setContentsMargins(0, 0, 0, 0)
        self.lfbChipsLayout.setObjectName("lfbChipsLayout")
        self.gridLayout.addWidget(self.horizontalWidget, 8, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lfbTextFieldError.setText(_translate("Form", "ErrorLabel"))
        self.lfbTextFieldDescriptionBtn.setText(_translate("Form", "i"))
        self.lfbTextFieldHelp.setText(_translate("Form", "Text content in QLabel can wrap lines "))
        self.lfbTextFieldSuccess.setText(_translate("Form", "SuccessLabel"))
        self.lfbTextFieldLabel.setText(_translate("Form", "TextLabel"))
