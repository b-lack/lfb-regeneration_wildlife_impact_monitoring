# Form implementation generated from reading ui file '/Users/b-mac/sites/lfb/qgis-4-DAU/gui/gnssPluginWidget.ui'
#
# Created by: PyQt5 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_gnssForm(object):
    def setupUi(self, gnssForm):
        gnssForm.setObjectName("gnssForm")
        gnssForm.resize(320, 240)
        self.progressBar = QtWidgets.QProgressBar(parent=gnssForm)
        self.progressBar.setGeometry(QtCore.QRect(90, 100, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(gnssForm)
        QtCore.QMetaObject.connectSlotsByName(gnssForm)

    def retranslateUi(self, gnssForm):
        _translate = QtCore.QCoreApplication.translate
        gnssForm.setWindowTitle(_translate("gnssForm", "Form"))
