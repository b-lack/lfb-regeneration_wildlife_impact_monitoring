# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gerrit/Sites/lfb/lfb-regeneration_wildlife_impact_monitoring/lfb_regeneration_wildlife_impact/gui/form/textfield.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1046, 657)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 20, 0, 20)
        self.gridLayout.setObjectName("gridLayout")
        self.lfbTextFieldUnit = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        self.lfbTextFieldUnit.setFont(font)
        self.lfbTextFieldUnit.setText("")
        self.lfbTextFieldUnit.setObjectName("lfbTextFieldUnit")
        self.gridLayout.addWidget(self.lfbTextFieldUnit, 1, 2, 1, 1)
        self.lfbTextFieldHelp = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfbTextFieldHelp.sizePolicy().hasHeightForWidth())
        self.lfbTextFieldHelp.setSizePolicy(sizePolicy)
        self.lfbTextFieldHelp.setWordWrap(True)
        self.lfbTextFieldHelp.setObjectName("lfbTextFieldHelp")
        self.gridLayout.addWidget(self.lfbTextFieldHelp, 2, 1, 1, 1)
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
        self.lfbTextFieldDescriptionBtn.setAutoRaise(False)
        self.lfbTextFieldDescriptionBtn.setObjectName("lfbTextFieldDescriptionBtn")
        self.gridLayout.addWidget(self.lfbTextFieldDescriptionBtn, 1, 0, 1, 1)
        self.lfbTextField = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfbTextField.sizePolicy().hasHeightForWidth())
        self.lfbTextField.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lfbTextField.setFont(font)
        self.lfbTextField.setStyleSheet("QLineEdit {\n"
"    border: 3px solid grey;\n"
"    border-radius: 10px;\n"
"    padding:10px;\n"
"    font-size: 20pt;\n"
"}")
        self.lfbTextField.setText("")
        self.lfbTextField.setPlaceholderText("")
        self.lfbTextField.setClearButtonEnabled(True)
        self.lfbTextField.setObjectName("lfbTextField")
        self.gridLayout.addWidget(self.lfbTextField, 1, 1, 1, 1)
        self.lfbTextFieldSuccess = QtWidgets.QLabel(Form)
        self.lfbTextFieldSuccess.setStyleSheet("color: green;")
        self.lfbTextFieldSuccess.setWordWrap(True)
        self.lfbTextFieldSuccess.setObjectName("lfbTextFieldSuccess")
        self.gridLayout.addWidget(self.lfbTextFieldSuccess, 4, 1, 1, 1)
        self.lfbTextFieldLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lfbTextFieldLabel.setFont(font)
        self.lfbTextFieldLabel.setObjectName("lfbTextFieldLabel")
        self.gridLayout.addWidget(self.lfbTextFieldLabel, 0, 1, 1, 1)
        self.lfbTextFieldError = QtWidgets.QLabel(Form)
        self.lfbTextFieldError.setStyleSheet("color: red;")
        self.lfbTextFieldError.setWordWrap(True)
        self.lfbTextFieldError.setObjectName("lfbTextFieldError")
        self.gridLayout.addWidget(self.lfbTextFieldError, 3, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lfbTextFieldHelp.setText(_translate("Form", "Text content in QLabel can wrap lines along word boundaries with the wordWrap property. By default, word wrap is disabled. To enable it use setWordWrap():\n"
"\n"
""))
        self.lfbTextFieldDescriptionBtn.setText(_translate("Form", "i"))
        self.lfbTextFieldSuccess.setText(_translate("Form", "SuccessLabel"))
        self.lfbTextFieldLabel.setText(_translate("Form", "TextLabel"))
        self.lfbTextFieldError.setText(_translate("Form", "ErrorLabel"))