# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddFace.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import MainPage
import AddFacialImages
import exaction
import dataGeneration
import SVM

#from CameraCapture import cameraCapture
#ToFix: lineEdit and LineEdit_2 are for First and Last Names, should be named
class Ui_addPersonPage(object):
    #opens up the MainPage
    def backToMainPage(self, addPersonPage):
        self.window = QtWidgets.QWidget()
        self.ui = MainPage.Ui_mainPage()
        self.ui.setupUi(self.window)
        self.window.show()
        addPersonPage.close()
    #opens up the add facial images page
    def goToAddFaceImage(self):
        self.window = QtWidgets.QWidget()
        self.ui = AddFacialImages.Ui_NewFacePicture()
        self.ui.setupUi(self.window)
        self.window.show()
    #Check if name is valid, if it is add camera
    def continueAddFaceImage(self):
        firstName = self.lineEdit.text()
        lastName = self.lineEdit_2.text()
        if not firstName or not lastName:
            self.errorLbl.setText("<font color='red'>Please enter a full name</font>")
        else:
            lock = True
            lock1 = True
            lock = exaction.webcamScreenshot(firstName + ' ' + lastName)
            while lock:
                pass
            if not lock:
                lock1 = dataGeneration.dataGeneration()
                while lock1:
                    pass
                if not lock1:
                    SVM.SVM()
            
    def setupUi(self, addPersonPage):
        addPersonPage.setObjectName("addPersonPage")
        addPersonPage.resize(571, 460)
        addPersonPage.setStyleSheet("background-color: rgb(67, 94, 144);")
        self.gridLayout = QtWidgets.QGridLayout(addPersonPage)
        self.gridLayout.setObjectName("gridLayout")
        self.continueBtn = QtWidgets.QPushButton(addPersonPage)
        self.continueBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.continueBtn.setObjectName("continueBtn")
        self.gridLayout.addWidget(self.continueBtn, 6, 0, 1, 1)
        self.backBtn = QtWidgets.QPushButton(addPersonPage)
        self.backBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.backBtn.setObjectName("backBtn")
        #go back to main menu when back button is clicked
        self.backBtn.clicked.connect(lambda: self.backToMainPage(addPersonPage))
        self.continueBtn.clicked.connect(self.continueAddFaceImage)
        self.gridLayout.addWidget(self.backBtn, 8, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(addPersonPage)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(addPersonPage)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.firstNamelbl = QtWidgets.QLabel(addPersonPage)
        self.firstNamelbl.setObjectName("firstNamelbl")
        self.gridLayout.addWidget(self.firstNamelbl, 2, 0, 1, 1)
        self.lastNameLbl = QtWidgets.QLabel(addPersonPage)
        self.lastNameLbl.setObjectName("lastNameLbl")
        self.gridLayout.addWidget(self.lastNameLbl, 4, 0, 1, 1)
        self.whatNameLbl = QtWidgets.QLabel(addPersonPage)
        self.whatNameLbl.setObjectName("whatNameLbl")
        self.gridLayout.addWidget(self.whatNameLbl, 0, 0, 1, 1)
        self.errorLbl = QtWidgets.QLabel(addPersonPage)
        self.errorLbl.setObjectName("errorLbl")
        self.gridLayout.addWidget(self.errorLbl, 5, 0, 1, 1)

        self.retranslateUi(addPersonPage)
        QtCore.QMetaObject.connectSlotsByName(addPersonPage)

    def retranslateUi(self, addPersonPage):
        _translate = QtCore.QCoreApplication.translate
        addPersonPage.setWindowTitle(_translate("addPersonPage", "AddNewFace"))
        self.continueBtn.setText(_translate("addPersonPage", "Continue"))
        self.backBtn.setText(_translate("addPersonPage", "Back"))
        self.firstNamelbl.setText(_translate("addPersonPage", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">First Name</span></p></body></html>"))
        self.lastNameLbl.setText(_translate("addPersonPage", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Last Name</span></p></body></html>"))
        self.whatNameLbl.setText(_translate("addPersonPage", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">What is</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">your</span></p><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Name?</span></p></body></html>"))
        self.errorLbl.setText(_translate("addPersonPage", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addPersonPage = QtWidgets.QWidget()
    ui = Ui_addPersonPage()
    ui.setupUi(addPersonPage)
    addPersonPage.show()
    sys.exit(app.exec_())

