# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CameraRecognition.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import MainPage


class Ui_camRecognitionPage(object):
    def backToMainPage(self):
        self.window = QtWidgets.QWidget()
        self.ui = MainPage.Ui_mainPage()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, camRecognitionPage):
        camRecognitionPage.setObjectName("camRecognitionPage")
        camRecognitionPage.resize(621, 456)
        camRecognitionPage.setStyleSheet("background-color: rgb(67, 94, 144);")
        self.gridLayout = QtWidgets.QGridLayout(camRecognitionPage)
        self.gridLayout.setObjectName("gridLayout")
        self.cameraView = QtWidgets.QGraphicsView(camRecognitionPage)
        self.cameraView.setObjectName("cameraView")
        self.gridLayout.addWidget(self.cameraView, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(camRecognitionPage)
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 1, 1, 1)
        self.stopBtn = QtWidgets.QPushButton(camRecognitionPage)
        self.stopBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.stopBtn.setObjectName("stopBtn")
        self.gridLayout.addWidget(self.stopBtn, 1, 0, 1, 1)
        self.backBtn = QtWidgets.QPushButton(camRecognitionPage)
        self.backBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.backBtn.setObjectName("backBtn")
        self.gridLayout.addWidget(self.backBtn, 1, 1, 1, 1)
        #go back to main page
        self.backBtn.clicked.connect(self.backToMainPage)
        
        self.retranslateUi(camRecognitionPage)
        QtCore.QMetaObject.connectSlotsByName(camRecognitionPage)

    def retranslateUi(self, camRecognitionPage):
        _translate = QtCore.QCoreApplication.translate
        camRecognitionPage.setWindowTitle(_translate("camRecognitionPage", "CameraRecognition"))
        self.stopBtn.setText(_translate("camRecognitionPage", "Stop"))
        self.backBtn.setText(_translate("camRecognitionPage", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    camRecognitionPage = QtWidgets.QWidget()
    ui = Ui_camRecognitionPage()
    ui.setupUi(camRecognitionPage)
    camRecognitionPage.show()
    sys.exit(app.exec_())

