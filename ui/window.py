# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Tue Apr 21 14:45:24 2015
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # Create the MainWindow
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(710, 569)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))

        # Create the window to display the graph
        self.mplwindow = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwindow.sizePolicy().hasHeightForWidth())
        self.mplwindow.setSizePolicy(sizePolicy)
        self.mplwindow.setMinimumSize(QtCore.QSize(0, 200))
        self.mplwindow.setMaximumSize(QtCore.QSize(16777215, 500))
        self.mplwindow.setObjectName(_fromUtf8("mplwindow"))

        # Layout for graph display
        self.mplvl = QtGui.QVBoxLayout(self.mplwindow)
        self.mplvl.setMargin(0)
        self.mplvl.setObjectName(_fromUtf8("mplvl"))
        self.gridLayout_2.addWidget(self.mplwindow, 0, 0, 1, 1, QtCore.Qt.AlignTop)

        # Create container to hold the buttons and text box
        self.container = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.container.sizePolicy().hasHeightForWidth())
        self.container.setSizePolicy(sizePolicy)
        self.container.setTitle(_fromUtf8(""))
        self.container.setObjectName(_fromUtf8("container"))

        # Layout for the button container
        self.horizontalLayout = QtGui.QHBoxLayout(self.container)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        # Create the buttons
        self.buttons = QtGui.QGroupBox(self.container)
        self.buttons.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttons.sizePolicy().hasHeightForWidth())
        self.buttons.setSizePolicy(sizePolicy)
        self.buttons.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buttons.setTitle(_fromUtf8(""))
        self.buttons.setObjectName(_fromUtf8("buttons"))

        # Set layout for buttons
        self.buttons_layout = QtGui.QVBoxLayout(self.buttons)
        self.buttons_layout.setObjectName(_fromUtf8("buttons_layout"))

        # Create combo box (drop down menu)
        self.combos = QtGui.QComboBox(self.buttons)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combos.sizePolicy().hasHeightForWidth())
        self.combos.setSizePolicy(sizePolicy)
        self.combos.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.combos.setObjectName(_fromUtf8("combos"))
        self.buttons_layout.addWidget(self.combos)

        # Create the save button
        self.save_button = QtGui.QPushButton(self.buttons)
        self.save_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.save_button.setObjectName(_fromUtf8("save_button"))
        self.buttons_layout.addWidget(self.save_button)

        # Create the display count button
        self.display_tweet_count = QtGui.QPushButton(self.buttons)
        self.display_tweet_count.setObjectName(_fromUtf8("display_tweet_count"))
        self.buttons_layout.addWidget(self.display_tweet_count)
        self.horizontalLayout.addWidget(self.buttons)

        # Create the text box (displays the tweets and counts
        self.text_edit = QtGui.QPlainTextEdit(self.container)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_edit.sizePolicy().hasHeightForWidth())
        self.text_edit.setSizePolicy(sizePolicy)
        self.text_edit.setMinimumSize(QtCore.QSize(400, 200))
        self.text_edit.setObjectName(_fromUtf8("text_edit"))
        self.horizontalLayout.addWidget(self.text_edit)
        self.gridLayout_2.addWidget(self.container, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.save_button.setText(_translate("MainWindow", "Save", None))
        self.display_tweet_count.setText(_translate("MainWindow", "Results", None))

