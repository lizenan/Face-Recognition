# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddFacialImages.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import AddFace

class Ui_NewFacePicture(object):
    def backToAddFace(self):
        self.window = QtWidgets.QWidget()
        self.ui = AddFace.Ui_addPersonPage()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, NewFacePicture):
        NewFacePicture.setObjectName("NewFacePicture")
        NewFacePicture.resize(1042, 893)
        NewFacePicture.setStyleSheet("background-color: rgb(67, 94, 144);")
        self.gridLayout = QtWidgets.QGridLayout(NewFacePicture)
        self.gridLayout.setObjectName("gridLayout")
        self.addPhotoBtn = QtWidgets.QPushButton(NewFacePicture)
        self.addPhotoBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.addPhotoBtn.setObjectName("addPhotoBtn")
        self.gridLayout.addWidget(self.addPhotoBtn, 3, 0, 1, 1)
        self.prevPhotoView = QtWidgets.QGraphicsView(NewFacePicture)
        self.prevPhotoView.setObjectName("prevPhotoView")
        self.gridLayout.addWidget(self.prevPhotoView, 1, 0, 1, 1)
        self.cameraView = QtWidgets.QGraphicsView(NewFacePicture)
        self.cameraView.setObjectName("cameraView")
        self.gridLayout.addWidget(self.cameraView, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.backBtn = QtWidgets.QPushButton(NewFacePicture)
        self.backBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.backBtn.setObjectName("backBtn")
        #go back to AddFace
        self.backBtn.clicked.connect(self.backToAddFace)
        self.horizontalLayout_2.addWidget(self.backBtn)
        self.doneBtn = QtWidgets.QPushButton(NewFacePicture)
        self.doneBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.doneBtn.setObjectName("doneBtn")
        self.horizontalLayout_2.addWidget(self.doneBtn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 0, 1, 1)
        self.takePicBtn = QtWidgets.QPushButton(NewFacePicture)
        self.takePicBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.takePicBtn.setObjectName("takePicBtn")
        self.gridLayout.addWidget(self.takePicBtn, 2, 0, 1, 1)
        self.errorLbl = QtWidgets.QLabel(NewFacePicture)
        self.errorLbl.setObjectName("errorLbl")
        self.gridLayout.addWidget(self.errorLbl, 4, 0, 1, 1)

        self.retranslateUi(NewFacePicture)
        QtCore.QMetaObject.connectSlotsByName(NewFacePicture)

    def retranslateUi(self, NewFacePicture):
        _translate = QtCore.QCoreApplication.translate
        NewFacePicture.setWindowTitle(_translate("NewFacePicture", "AddNewFace"))
        self.addPhotoBtn.setText(_translate("NewFacePicture", "Add Photo"))
        self.backBtn.setText(_translate("NewFacePicture", "Back"))
        self.doneBtn.setText(_translate("NewFacePicture", "Done"))
        self.takePicBtn.setText(_translate("NewFacePicture", "Take Picture"))
        self.errorLbl.setText(_translate("NewFacePicture", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewFacePicture = QtWidgets.QWidget()
    ui = Ui_NewFacePicture()
    ui.setupUi(NewFacePicture)
    NewFacePicture.show()
    sys.exit(app.exec_())

