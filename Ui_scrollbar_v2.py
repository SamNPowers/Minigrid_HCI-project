# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scrollbar_v2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 660)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.buttons_Hlayout = QtWidgets.QHBoxLayout()
        self.buttons_Hlayout.setContentsMargins(-1, -1, -1, 0)
        self.buttons_Hlayout.setObjectName("buttons_Hlayout")
        self.new_game_pb = QtWidgets.QPushButton(self.centralwidget)
        self.new_game_pb.setObjectName("new_game_pb")
        self.buttons_Hlayout.addWidget(self.new_game_pb, 0, QtCore.Qt.AlignRight)
        self.train_pb = QtWidgets.QPushButton(self.centralwidget)
        self.train_pb.setObjectName("train_pb")
        self.buttons_Hlayout.addWidget(self.train_pb, 0, QtCore.Qt.AlignRight)
        self.gridLayout_4.addLayout(self.buttons_Hlayout, 8, 0, 1, 1)
        self.main_horizontalLayout = QtWidgets.QHBoxLayout()
        self.main_horizontalLayout.setContentsMargins(-1, 0, 0, 0)
        self.main_horizontalLayout.setObjectName("main_horizontalLayout")
        self.games_scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.games_scrollArea.sizePolicy().hasHeightForWidth())
        self.games_scrollArea.setSizePolicy(sizePolicy)
        self.games_scrollArea.setWidgetResizable(True)
        self.games_scrollArea.setObjectName("games_scrollArea")
        self.games_verticalW = QtWidgets.QWidget()
        self.games_verticalW.setGeometry(QtCore.QRect(0, 0, 548, 534))
        self.games_verticalW.setObjectName("games_verticalW")
        self.games_verticalLayout = QtWidgets.QVBoxLayout(self.games_verticalW)
        self.games_verticalLayout.setObjectName("games_verticalLayout")
        self.horizontalLayout_game1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_game1.setObjectName("horizontalLayout_game1")
        self.game_1 = QtWidgets.QLabel(self.games_verticalW)
        self.game_1.setObjectName("game_1")
        self.horizontalLayout_game1.addWidget(self.game_1)
        self.image_1 = QtWidgets.QLabel(self.games_verticalW)
        self.image_1.setObjectName("image_1")
        self.horizontalLayout_game1.addWidget(self.image_1)
        self.info_1 = QtWidgets.QPushButton(self.games_verticalW)
        self.info_1.setObjectName("info_1")
        self.horizontalLayout_game1.addWidget(self.info_1)
        self.remove_game_pb = QtWidgets.QPushButton(self.games_verticalW)
        self.remove_game_pb.setObjectName("remove_game_pb")
        self.horizontalLayout_game1.addWidget(self.remove_game_pb)
        self.move_to_rank_1 = QtWidgets.QPushButton(self.games_verticalW)
        self.move_to_rank_1.setObjectName("move_to_rank_1")
        self.horizontalLayout_game1.addWidget(self.move_to_rank_1)
        self.games_verticalLayout.addLayout(self.horizontalLayout_game1)
        self.horizontalLayout_game2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_game2.setObjectName("horizontalLayout_game2")
        self.label_4 = QtWidgets.QLabel(self.games_verticalW)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_game2.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.games_verticalW)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_game2.addWidget(self.label_3)
        self.pushButton_6 = QtWidgets.QPushButton(self.games_verticalW)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_game2.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.games_verticalW)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_game2.addWidget(self.pushButton_5)
        self.games_verticalLayout.addLayout(self.horizontalLayout_game2)
        self.games_scrollArea.setWidget(self.games_verticalW)
        self.main_horizontalLayout.addWidget(self.games_scrollArea)
        self.game_ranking_scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.game_ranking_scrollArea.sizePolicy().hasHeightForWidth())
        self.game_ranking_scrollArea.setSizePolicy(sizePolicy)
        self.game_ranking_scrollArea.setWidgetResizable(True)
        self.game_ranking_scrollArea.setObjectName("game_ranking_scrollArea")
        self.ranking_verticalW = QtWidgets.QWidget()
        self.ranking_verticalW.setGeometry(QtCore.QRect(0, 0, 547, 534))
        self.ranking_verticalW.setObjectName("ranking_verticalW")
        self.ranking_verticalLayout = QtWidgets.QVBoxLayout(self.ranking_verticalW)
        self.ranking_verticalLayout.setObjectName("ranking_verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.ranking_verticalW)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_4.addWidget(self.pushButton_7)
        self.label_6 = QtWidgets.QLabel(self.ranking_verticalW)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.ranking_verticalW)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.pushButton_2 = QtWidgets.QPushButton(self.ranking_verticalW)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_8 = QtWidgets.QPushButton(self.ranking_verticalW)
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setDefault(False)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_4.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.ranking_verticalW)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_4.addWidget(self.pushButton_9)
        self.ranking_verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_10 = QtWidgets.QPushButton(self.ranking_verticalW)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_5.addWidget(self.pushButton_10)
        self.label_7 = QtWidgets.QLabel(self.ranking_verticalW)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.pushButton_12 = QtWidgets.QPushButton(self.ranking_verticalW)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_5.addWidget(self.pushButton_12)
        self.pushButton_11 = QtWidgets.QPushButton(self.ranking_verticalW)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_5.addWidget(self.pushButton_11)
        self.ranking_verticalLayout.addLayout(self.horizontalLayout_5)
        self.pushButton = QtWidgets.QPushButton(self.ranking_verticalW)
        self.pushButton.setObjectName("pushButton")
        self.ranking_verticalLayout.addWidget(self.pushButton)
        self.game_ranking_scrollArea.setWidget(self.ranking_verticalW)
        self.main_horizontalLayout.addWidget(self.game_ranking_scrollArea)
        self.gridLayout_4.addLayout(self.main_horizontalLayout, 6, 0, 1, 1)
        self.titles_Hlayout = QtWidgets.QHBoxLayout()
        self.titles_Hlayout.setContentsMargins(-1, -1, -1, 0)
        self.titles_Hlayout.setObjectName("titles_Hlayout")
        self.game_list_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.game_list_title.setFont(font)
        self.game_list_title.setObjectName("game_list_title")
        self.titles_Hlayout.addWidget(self.game_list_title)
        self.game_ranking_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.game_ranking_title.setFont(font)
        self.game_ranking_title.setObjectName("game_ranking_title")
        self.titles_Hlayout.addWidget(self.game_ranking_title)
        self.gridLayout_4.addLayout(self.titles_Hlayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1125, 22))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.new_game_pb.setText(_translate("MainWindow", "New game"))
        self.train_pb.setText(_translate("MainWindow", "Train"))
        self.game_1.setText(_translate("MainWindow", "game 1"))
        self.image_1.setText(_translate("MainWindow", "image 1"))
        self.info_1.setText(_translate("MainWindow", "info"))
        self.remove_game_pb.setText(_translate("MainWindow", "remove"))
        self.move_to_rank_1.setText(_translate("MainWindow", "->"))
        self.label_4.setText(_translate("MainWindow", "game 2"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "->"))
        self.pushButton_7.setText(_translate("MainWindow", "<-"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_8.setText(_translate("MainWindow", "move up"))
        self.pushButton_9.setText(_translate("MainWindow", "move down"))
        self.pushButton_10.setText(_translate("MainWindow", "PushButton"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_12.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_11.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.game_list_title.setText(_translate("MainWindow", "Game list"))
        self.game_ranking_title.setText(_translate("MainWindow", "Game ranking"))

