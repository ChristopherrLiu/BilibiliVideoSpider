# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import qtawesome as qta

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498, 381)
        font = QFont()
        font.setFamily("微软雅黑")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.leftWidget = QtWidgets.QWidget(self.centralWidget)
        self.leftWidget.setMaximumSize(QtCore.QSize(70, 16777215))
        self.leftWidget.setObjectName("leftWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.leftWidget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.AVPpushButton = QtWidgets.QPushButton(qta.icon('fa.film',color='white'), "", self.leftWidget)
        self.AVPpushButton.setObjectName("AVPpushButton")
        self.gridLayout_3.addWidget(self.AVPpushButton, 20, 0, 20, 60)
        self.smallerPushButton = QtWidgets.QPushButton(self.leftWidget)
        self.smallerPushButton.setObjectName("smallerPushButton")
        self.smallerPushButton.setGeometry(QtCore.QRect(35, 10, 14, 14))
        self.closePushButton = QtWidgets.QPushButton(self.leftWidget)
        self.closePushButton.setObjectName("closePushButton")
        self.closePushButton.setGeometry(QtCore.QRect(5, 10, 14, 14))
        self.UPPushButton = QtWidgets.QPushButton(qta.icon('fa.star',color='white'), "", self.leftWidget)
        self.UPPushButton.setObjectName("UPPushButton")
        self.gridLayout_3.addWidget(self.UPPushButton, 40, 0, 20, 60)
        self.AboutPushButton = QtWidgets.QPushButton(qta.icon('fa.question',color='white'), "", self.leftWidget)
        self.AboutPushButton.setObjectName("AboutPushButton")
        self.gridLayout_3.addWidget(self.AboutPushButton, 60, 0, 20, 60)
        self.gridLayout.addWidget(self.leftWidget, 0, 0, 1, 1)
        self.rightWidget = QtWidgets.QWidget(self.centralWidget)
        self.rightWidget.setObjectName("rightWidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.rightWidget)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.rightWidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.AVLabel = QtWidgets.QLabel(self.page)
        self.AVLabel.setGeometry(QtCore.QRect(10, 20, 51, 21))
        self.AVLabel.setObjectName("AVLabel")
        self.AVLineEdit = QtWidgets.QLineEdit(self.page)
        self.AVLineEdit.setGeometry(QtCore.QRect(70, 20, 221, 20))
        self.AVLineEdit.setObjectName("AVLineEdit")
        self.searchPushButton = QtWidgets.QPushButton(self.page)
        self.searchPushButton.setGeometry(QtCore.QRect(300, 20, 71, 21))
        self.searchPushButton.setObjectName("searchPushButton")
        self.titleLineEdit = QtWidgets.QLineEdit(self.page)
        self.titleLineEdit.setGeometry(QtCore.QRect(70, 60, 301, 20))
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.titleLabel = QtWidgets.QLabel(self.page)
        self.titleLabel.setGeometry(QtCore.QRect(10, 60, 51, 21))
        self.titleLabel.setObjectName("titleLabel")
        self.authorLineEdit = QtWidgets.QLineEdit(self.page)
        self.authorLineEdit.setGeometry(QtCore.QRect(70, 100, 301, 20))
        self.authorLineEdit.setText("")
        self.authorLineEdit.setObjectName("authorLineEdit")
        self.authorLabel = QtWidgets.QLabel(self.page)
        self.authorLabel.setGeometry(QtCore.QRect(10, 100, 51, 21))
        self.authorLabel.setObjectName("authorLabel")
        self.descriptionTextEdit = QtWidgets.QTextEdit(self.page)
        self.descriptionTextEdit.setGeometry(QtCore.QRect(70, 140, 301, 51))
        self.descriptionTextEdit.setObjectName("descriptionTextEdit")
        self.descriptionLabel = QtWidgets.QLabel(self.page)
        self.descriptionLabel.setGeometry(QtCore.QRect(10, 140, 51, 21))
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.coverLineEdit = QtWidgets.QLineEdit(self.page)
        self.coverLineEdit.setGeometry(QtCore.QRect(70, 210, 301, 21))
        self.coverLineEdit.setObjectName("coverLineEdit")
        self.coverLabel = QtWidgets.QLabel(self.page)
        self.coverLabel.setGeometry(QtCore.QRect(10, 210, 51, 21))
        self.coverLabel.setObjectName("coverLabel")
        self.listView = QtWidgets.QListView(self.page)
        self.listView.setGeometry(QtCore.QRect(10, 250, 361, 51))
        self.listView.setObjectName("listView")
        self.downloadPushButton = QtWidgets.QPushButton(self.page)
        self.downloadPushButton.setGeometry(QtCore.QRect(310, 310, 61, 21))
        self.downloadPushButton.setObjectName("downloadPushButton")
        self.savePicPushButton = QtWidgets.QPushButton(self.page)
        self.savePicPushButton.setGeometry(QtCore.QRect(10, 310, 61, 21))
        self.savePicPushButton.setObjectName("savePicPushButton")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.uidLineEdit = QtWidgets.QLineEdit(self.page_2)
        self.uidLineEdit.setGeometry(QtCore.QRect(70, 20, 221, 20))
        self.uidLineEdit.setObjectName("uidLineEdit")
        self.searchPushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.searchPushButton_2.setGeometry(QtCore.QRect(300, 20, 71, 21))
        self.searchPushButton_2.setObjectName("searchPushButton_2")
        self.uidLabel = QtWidgets.QLabel(self.page_2)
        self.uidLabel.setGeometry(QtCore.QRect(10, 20, 51, 21))
        self.uidLabel.setObjectName("uidLabel")
        self.UPNameLineEdit = QtWidgets.QLineEdit(self.page_2)
        self.UPNameLineEdit.setGeometry(QtCore.QRect(70, 60, 280, 20))
        self.UPNameLineEdit.setObjectName("UPNameLineEdit")
        self.UPNameLineEdit.setFont(font)
        self.UPNameLabel = QtWidgets.QLabel(self.page_2)
        self.UPNameLabel.setGeometry(QtCore.QRect(10, 60, 51, 21))
        self.UPNameLabel.setObjectName("UPNameLabel")
        self.upFaceLabel = QtWidgets.QLabel(self.page_2)
        self.upFaceLabel.setGeometry(QtCore.QRect(330, 50, 40, 40))
        self.upFaceLabel.setObjectName("upFaceLabel")
        self.upSignLabel = QtWidgets.QLabel(self.page_2)
        self.upSignLabel.setGeometry(QtCore.QRect(10, 100, 51, 21))
        self.upSignLabel.setObjectName("upSignLabel")
        self.upSignTextEdit = QtWidgets.QTextEdit(self.page_2)
        self.upSignTextEdit.setGeometry(QtCore.QRect(70, 100, 316, 40))
        self.upSignTextEdit.setObjectName("upSignTextEdit")
        self.upSignTextEdit.setFont(font)
        self.listWidget = QtWidgets.QListWidget(self.page_2)
        self.listWidget.setGeometry(QtCore.QRect(10, 140, 361, 191))
        self.listWidget.setObjectName("listWidget")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_5.addWidget(self.stackedWidget, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.rightWidget, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", ""))
        self.AVPpushButton.setText(_translate("MainWindow", "av号"))
        self.smallerPushButton.setText(_translate("MainWindow", ""))
        self.closePushButton.setText(_translate("MainWindow", ""))
        self.UPPushButton.setText(_translate("MainWindow", "up主"))
        self.AboutPushButton.setText(_translate("MainWindow", "关于"))
        self.AVLabel.setText(_translate("MainWindow", "av号："))
        self.searchPushButton.setText(_translate("MainWindow", "查询"))
        self.titleLabel.setText(_translate("MainWindow", "标题："))
        self.authorLabel.setText(_translate("MainWindow", "作者："))
        self.descriptionLabel.setText(_translate("MainWindow", "简介："))
        self.coverLabel.setText(_translate("MainWindow", "封面地址："))
        self.downloadPushButton.setText(_translate("MainWindow", "下载"))
        self.savePicPushButton.setText(_translate("MainWindow", "保存封面"))
        self.searchPushButton_2.setText(_translate("MainWindow", "查询"))
        self.uidLabel.setText(_translate("MainWindow", "UID："))
        self.UPNameLabel.setText(_translate("MainWindow", "账号："))
        self.upSignLabel.setText(_translate("MainWindow", "个性签名："))