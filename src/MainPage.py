# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import CameraRecognition
import AddFace
import faceRecognition
import os
import AboutPage

def find(name, path):
    for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)

class Ui_mainPage(object):
    
    def toAboutPage(self, mainPage):
        self.window = QtWidgets.QWidget()
        self.ui = AboutPage.Ui_aboutPage()
        self.ui.setupUi(self.window)
        self.window.show()
        mainPage.close()
    
    #go to facial recognition page
    def toRecognition(self, mainPage):
        self.window = QtWidgets.QWidget()
        self.ui = CameraRecognition.Ui_camRecognitionPage()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def recognitionCam(self):
        faceRecognition.faceRecognition()
        
        
    #go to AddFace page
    def toAddFace(self, mainPage):
        self.window = QtWidgets.QWidget()
        self.ui = AddFace.Ui_addPersonPage()
        self.ui.setupUi(self.window)
        self.window.show()
        mainPage.close()
        
    def setupUi(self, mainPage):
        mainPage.setObjectName("mainPage")
        mainPage.resize(521, 351)
        mainPage.setAutoFillBackground(False)
        mainPage.setStyleSheet("background-color: rgb(67, 94, 144);")
        self.gridLayout = QtWidgets.QGridLayout(mainPage)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(mainPage)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 2, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.gridLayout.addLayout(self.formLayout, 0, 1, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.gridLayout.addLayout(self.formLayout_2, 0, 3, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.startRecBtn = QtWidgets.QPushButton(mainPage)
        self.startRecBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")   
        self.startRecBtn.setObjectName("startRecBtn")
        self.verticalLayout.addWidget(self.startRecBtn)
        self.addFaceBtn = QtWidgets.QPushButton(mainPage)
        self.addFaceBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.addFaceBtn.setObjectName("addFaceBtn")
        #go to other pages
        self.startRecBtn.clicked.connect(self.recognitionCam)  
        self.addFaceBtn.clicked.connect(lambda: self.toAddFace(mainPage))
        
        self.verticalLayout.addWidget(self.addFaceBtn)
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)
        self.aboutBtn = QtWidgets.QPushButton(mainPage)
        self.aboutBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.aboutBtn.setObjectName("aboutBtn")
        self.aboutBtn.clicked.connect(lambda: self.toAboutPage(mainPage))
        self.gridLayout.addWidget(self.aboutBtn, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(mainPage)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(mainPage)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)

        self.retranslateUi(mainPage)
        QtCore.QMetaObject.connectSlotsByName(mainPage)

    def retranslateUi(self, mainPage):
        _translate = QtCore.QCoreApplication.translate
        mainPage.setWindowTitle(_translate("mainPage", "MainPage"))
        self.label.setText(_translate("mainPage", "<html><head/><body><p><span style=\" font-size:48pt; color:#ffffff;\">Smile</span></p></body></html>"))
        self.startRecBtn.setText(_translate("mainPage", "Start Recognition"))
        self.addFaceBtn.setText(_translate("mainPage", "Add Face"))
        self.aboutBtn.setText(_translate("mainPage", "About"))
        self.label_2.setText(_translate("mainPage", "<html><head/><body><p><br/></p></body></html>"))
        self.label_3.setText(_translate("mainPage", "<html><head/><body><p><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainPage = QtWidgets.QWidget()
    ui = Ui_mainPage()
    ui.setupUi(mainPage)
    mainPage.show()
    sys.exit(app.exec_())

