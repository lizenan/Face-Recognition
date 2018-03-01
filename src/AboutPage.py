# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutPage.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import MainPage

class Ui_aboutPage(object):
    def backToMainPage(self, aboutPage):
        self.window = QtWidgets.QWidget()
        self.ui = MainPage.Ui_mainPage()
        self.ui.setupUi(self.window)
        self.window.show()
        aboutPage.close()
    
    def setupUi(self, aboutPage):
        aboutPage.setObjectName("aboutPage")
        aboutPage.resize(489, 309)
        aboutPage.setStyleSheet("background-color: rgb(67, 94, 144);")
        self.gridLayout = QtWidgets.QGridLayout(aboutPage)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(aboutPage)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.backBtn = QtWidgets.QPushButton(aboutPage)
        self.backBtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 255);")
        self.backBtn.setObjectName("backBtn")
        self.gridLayout.addWidget(self.backBtn, 1, 0, 1, 1)

        self.retranslateUi(aboutPage)
        QtCore.QMetaObject.connectSlotsByName(aboutPage)

    def retranslateUi(self, aboutPage):
        _translate = QtCore.QCoreApplication.translate
        aboutPage.setWindowTitle(_translate("aboutPage", "About"))
        self.textBrowser.setHtml(_translate("aboutPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Created for Computer Vision and Deep Learning at California State University, Fullerton. This application can recognize faces that have been added and examined.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">If your face is already added to the application, you can start recognition by clicking &quot;Start Recognition&quot; to begin. To close any camera window at anytime press q on your keyboard. If your face has yet to added click &quot;Add Face&quot; and enter your information. After entering your information a window with your pc camera should pop up. Move your face as much as possible while still keeping eye contact with the camera. When the window closes your face should be added.</span></p></body></html>"))
        self.backBtn.setText(_translate("aboutPage", "Back"))
        self.backBtn.clicked.connect(lambda: self.backToMainPage(aboutPage))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aboutPage = QtWidgets.QWidget()
    ui = Ui_aboutPage()
    ui.setupUi(aboutPage)
    aboutPage.show()
    sys.exit(app.exec_())
