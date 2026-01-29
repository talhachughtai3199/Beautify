# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fyp2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt
from PIL import Image, ImageEnhance
import cv2
import numpy as np
import os
from sklearn import tree
from sklearn.model_selection import train_test_split
import ctypes
import tensorflow as tf
#from PIL import Image,ImageFilter

#this object_detection is a folder that has this utils files
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

class Ui_fyp(object):
    w=0
    h=0
    filter_text=''
    flag=False
    path="string"
    indpath="C:/Beautify_temp_files"
    i=0
    typ='.jpg'
    concated_path="string"
    enhanced_im=2
    concated_temp_path="String"
    maxiter=0
    miniter=0
    concated_path_2="String"
    cropping = False
    rotation_count=1
    rotation_flag=False
    def setupUi(self, fyp):
        fyp.setObjectName("fyp")
        fyp.resize(1990, 1259)
        fyp.setSizeIncrement(QtCore.QSize(2, 1))
        fyp.setAutoFillBackground(False)
        fyp.setStyleSheet("QMainWindow{ background-color:rgb(30, 30, 30); }\n"
"")
        self.centralwidget = QtWidgets.QWidget(fyp)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.redo = QtWidgets.QPushButton(self.frame_3)
        self.redo.setMinimumSize(QtCore.QSize(50, 30))
        self.redo.setStyleSheet("background-color : trasnparent ;\n"
"background : none ;\n"
"border : none;\n"
"background-repeat : none")
        self.redo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("undo copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redo.setIcon(icon)
        self.redo.setIconSize(QtCore.QSize(50, 25))
        self.redo.setObjectName("redo")
        self.gridLayout.addWidget(self.redo, 0, 4, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(1269, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 6, 1, 1)
        self.undo = QtWidgets.QPushButton(self.frame_3)
        self.undo.setMinimumSize(QtCore.QSize(50, 30))
        self.undo.setStyleSheet("background-color : trasnparent ;\n"
"background : none ;\n"
"border : none;\n"
"background-repeat : none")
        self.undo.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Redo copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undo.setIcon(icon1)
        self.undo.setIconSize(QtCore.QSize(50, 25))
        self.undo.setAutoDefault(False)
        self.undo.setObjectName("undo")
        self.gridLayout.addWidget(self.undo, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.cancel = QtWidgets.QPushButton(self.frame_3)
        self.cancel.setMinimumSize(QtCore.QSize(50, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(235, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(235, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        self.cancel.setPalette(palette)
        self.cancel.setObjectName("cancel")
        self.gridLayout.addWidget(self.cancel, 0, 7, 1, 1)
        self.saveimg = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveimg.sizePolicy().hasHeightForWidth())
        self.saveimg.setSizePolicy(sizePolicy)
        self.saveimg.setMinimumSize(QtCore.QSize(50, 30))
        self.saveimg.setStyleSheet("background-color : trasnparent ;\n"
"background : none ;\n"
"border : none;\n"
"background-repeat : none")
        self.saveimg.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Download_Document-512 copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveimg.setIcon(icon2)
        self.saveimg.setIconSize(QtCore.QSize(50, 30))
        self.saveimg.setObjectName("saveimg")
        self.gridLayout.addWidget(self.saveimg, 0, 1, 1, 1)
        self.close = QtWidgets.QPushButton(self.frame_3)
        self.close.setMinimumSize(QtCore.QSize(50, 30))
        self.close.setStyleSheet("background-color : trasnparent ;\n"
"background : none ;\n"
"border : none;\n"
"background-repeat : none")
        self.close.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("UI_Light_Close_menu-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("UI_Light_Close_menu-512.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.close.setIcon(icon3)
        self.close.setIconSize(QtCore.QSize(50, 50))
        self.close.setObjectName("close")
        self.gridLayout.addWidget(self.close, 0, 2, 1, 1)
        self.open = QtWidgets.QPushButton(self.frame_3)
        self.open.setMinimumSize(QtCore.QSize(50, 30))
        self.open.setMaximumSize(QtCore.QSize(75, 23))
        self.open.setStyleSheet("background-color : trasnparent ;\n"
"background : none ;\n"
"border : none;\n"
"background-repeat : none")
        self.open.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("171127-200 copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open.setIcon(icon4)
        self.open.setIconSize(QtCore.QSize(50, 30))
        self.open.setObjectName("open")
        self.gridLayout.addWidget(self.open, 0, 0, 1, 1)
        self.apply = QtWidgets.QPushButton(self.frame_3)
        self.apply.setMinimumSize(QtCore.QSize(50, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(235, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(235, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        self.apply.setPalette(palette)
        self.apply.setObjectName("apply")
        self.gridLayout.addWidget(self.apply, 0, 8, 1, 1)
        self.gridLayout_3.addWidget(self.frame_3, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("QFrame{ background-color:rgb(30, 30, 30); }\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.beautify = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.beautify.sizePolicy().hasHeightForWidth())
        self.beautify.setSizePolicy(sizePolicy)
        self.beautify.setMinimumSize(QtCore.QSize(40, 40))
        self.beautify.setAutoFillBackground(False)
        self.beautify.setStyleSheet("background-color : trasnparent ;\n"
"background : none ;\n"
"border : none;\n"
"background-repeat : none")
        self.beautify.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("audio copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.beautify.setIcon(icon5)
        self.beautify.setIconSize(QtCore.QSize(40, 40))
        self.beautify.setAutoRepeatDelay(0)
        self.beautify.setAutoRepeatInterval(0)
        self.beautify.setObjectName("beautify")
        self.verticalLayout.addWidget(self.beautify)
        self.filtertext = QtWidgets.QLineEdit(self.frame)
        self.filtertext.setMinimumSize(QtCore.QSize(80, 20))
        self.filtertext.setMaximumSize(QtCore.QSize(40, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 78, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 78, 78, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 78, 78))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 78, 78, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        self.filtertext.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.filtertext.setFont(font)
        self.filtertext.setAutoFillBackground(False)
        self.filtertext.setStyleSheet("QLineEdit{ background-color:rgb(30, 30, 30); }")
        self.filtertext.setCursorPosition(12)
        self.filtertext.setDragEnabled(False)
        self.filtertext.setReadOnly(True)
        self.filtertext.setObjectName("filtertext")
        self.verticalLayout.addWidget(self.filtertext)
        self.fix = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fix.sizePolicy().hasHeightForWidth())
        self.fix.setSizePolicy(sizePolicy)
        self.fix.setMinimumSize(QtCore.QSize(40, 40))
        self.fix.setStyleSheet("background-color : trasnparent ;\n"
"background : none ;\n"
"border : none;\n"
"background-repeat : none")
        self.fix.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Crop-2-icon copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fix.setIcon(icon6)
        self.fix.setIconSize(QtCore.QSize(40, 40))
        self.fix.setObjectName("fix")
        self.verticalLayout.addWidget(self.fix)
        self.fixtext = QtWidgets.QLineEdit(self.frame)
        self.fixtext.setMinimumSize(QtCore.QSize(80, 20))
        self.fixtext.setMaximumSize(QtCore.QSize(40, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        self.fixtext.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.fixtext.setFont(font)
        self.fixtext.setStyleSheet("QLineEdit{ background-color:rgb(30, 30, 30); }")
        self.fixtext.setDragEnabled(False)
        self.fixtext.setReadOnly(True)
        self.fixtext.setObjectName("fixtext")
        self.verticalLayout.addWidget(self.fixtext)
        self.filter = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filter.sizePolicy().hasHeightForWidth())
        self.filter.setSizePolicy(sizePolicy)
        self.filter.setMinimumSize(QtCore.QSize(40, 40))
        self.filter.setStyleSheet("background-color : trasnparent ;\n"
"background : none ;\n"
"border : none;\n"
"background-repeat : none")
        self.filter.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("135-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap("135-512.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.filter.setIcon(icon7)
        self.filter.setIconSize(QtCore.QSize(40, 40))
        self.filter.setObjectName("filter")
        self.verticalLayout.addWidget(self.filter)
        self.beautifytext = QtWidgets.QLineEdit(self.frame)
        self.beautifytext.setMinimumSize(QtCore.QSize(80, 20))
        self.beautifytext.setMaximumSize(QtCore.QSize(40, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        self.beautifytext.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.beautifytext.setFont(font)
        self.beautifytext.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.beautifytext.setDragEnabled(False)
        self.beautifytext.setReadOnly(True)
        self.beautifytext.setObjectName("beautifytext")
        self.verticalLayout.addWidget(self.beautifytext)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.slider = QtWidgets.QSlider(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider.sizePolicy().hasHeightForWidth())
        self.slider.setSizePolicy(sizePolicy)
        self.slider.setMinimumSize(QtCore.QSize(200, 40))
        self.slider.setMaximumSize(QtCore.QSize(600, 16777215))
        self.slider.setStyleSheet("")
        self.slider.setMinimum(-50)
        self.slider.setMaximum(50)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setInvertedAppearance(False)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider.setObjectName("slider")
        self.gridLayout_6.addWidget(self.slider, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.image = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setMinimumSize(QtCore.QSize(610, 300))
        self.image.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.image.setMouseTracking(False)
        self.image.setStyleSheet("QLabel{ background-color: rgb(30, 30, 30); }")
        self.image.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image.setLineWidth(4)
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("icon.jpg"))
        self.image.setScaledContents(False)
        self.image.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.image.setObjectName("image")
        self.w=self.image.width()
        self.h=self.image.height()
        self.gridLayout_6.addWidget(self.image, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 1, 1, 2, 1)
        self.compframe = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compframe.sizePolicy().hasHeightForWidth())
        self.compframe.setSizePolicy(sizePolicy)
        self.compframe.setAutoFillBackground(False)
        self.compframe.setStyleSheet("QFrame{ background-color:rgb(30, 30, 30); }\n"
"\n"
"")
        self.compframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.compframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.compframe.setObjectName("compframe")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.compframe)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.brightness = QtWidgets.QPushButton(self.compframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brightness.sizePolicy().hasHeightForWidth())
        self.brightness.setSizePolicy(sizePolicy)
        self.brightness.setMinimumSize(QtCore.QSize(40, 40))
        self.brightness.setMaximumSize(QtCore.QSize(40, 40))
        self.brightness.setStyleSheet("background-color : trasnparent ;\n"
"background : none ;\n"
"border : none;\n"
"background-repeat : none")
        self.brightness.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("img_514131.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.brightness.setIcon(icon8)
        self.brightness.setIconSize(QtCore.QSize(40, 40))
        self.brightness.setObjectName("brightness")
        self.gridLayout_2.addWidget(self.brightness, 14, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.contrast = QtWidgets.QPushButton(self.compframe)
        self.contrast.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contrast.sizePolicy().hasHeightForWidth())
        self.contrast.setSizePolicy(sizePolicy)
        self.contrast.setMinimumSize(QtCore.QSize(40, 40))
        self.contrast.setMaximumSize(QtCore.QSize(40, 40))
        self.contrast.setAutoFillBackground(False)
        self.contrast.setStyleSheet("background-color : trasnparent ;\n"
"background : none ;\n"
"border : none;\n"
"background-repeat : none\n"
"")
        self.contrast.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("contrast.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon9.addPixmap(QtGui.QPixmap("contrast.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.contrast.setIcon(icon9)
        self.contrast.setIconSize(QtCore.QSize(40, 40))
        self.contrast.setObjectName("contrast")
        self.gridLayout_2.addWidget(self.contrast, 11, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.crop = QtWidgets.QPushButton(self.compframe)
        self.crop.setMinimumSize(QtCore.QSize(40, 40))
        self.crop.setStyleSheet("background-color : trasnparent ;\n"
"background : none ;\n"
"border : none;\n"
"background-repeat : none\n"
"\n"
"")
        self.crop.setText("")
        self.crop.setIcon(icon6)
        self.crop.setIconSize(QtCore.QSize(40, 40))
        self.crop.setObjectName("crop")
        self.gridLayout_2.addWidget(self.crop, 6, 0, 1, 1)
        self.croptext = QtWidgets.QLineEdit(self.compframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.croptext.sizePolicy().hasHeightForWidth())
        self.croptext.setSizePolicy(sizePolicy)
        self.croptext.setMinimumSize(QtCore.QSize(80, 20))
        self.croptext.setMaximumSize(QtCore.QSize(70, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        self.croptext.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.croptext.setFont(font)
        self.croptext.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.croptext.setAutoFillBackground(False)
        self.croptext.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.croptext.setCursorPosition(12)
        self.croptext.setDragEnabled(False)
        self.croptext.setReadOnly(True)
        self.croptext.setObjectName("croptext")
        self.gridLayout_2.addWidget(self.croptext, 8, 0, 1, 1)
        self.spot = QtWidgets.QPushButton(self.compframe)
        self.spot.setMinimumSize(QtCore.QSize(40, 40))
        self.spot.setStyleSheet("background-color : trasnparent ;\n"
"background : none ;\n"
"border : none;\n"
"background-repeat : none\n"
"\n"
"")
        self.spot.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("Interface_Tools_Vol._3-35-512 copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.spot.setIcon(icon10)
        self.spot.setIconSize(QtCore.QSize(40, 40))
        self.spot.setObjectName("spot")
        self.gridLayout_2.addWidget(self.spot, 2, 0, 1, 1)
        self.faciatext = QtWidgets.QLineEdit(self.compframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.faciatext.sizePolicy().hasHeightForWidth())
        self.faciatext.setSizePolicy(sizePolicy)
        self.faciatext.setMinimumSize(QtCore.QSize(80, 20))
        self.faciatext.setMaximumSize(QtCore.QSize(70, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        self.faciatext.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.faciatext.setFont(font)
        self.faciatext.setToolTipDuration(-1)
        self.faciatext.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.faciatext.setStyleSheet("QLineEdit{ background-color:rgb(30, 30, 30); }")
        self.faciatext.setMaxLength(40)
        self.faciatext.setFrame(True)
        self.faciatext.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.faciatext.setCursorPosition(14)
        self.faciatext.setDragEnabled(False)
        self.faciatext.setReadOnly(True)
        self.faciatext.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.faciatext.setObjectName("faciatext")
        self.gridLayout_2.addWidget(self.faciatext, 5, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 20, 0, 1, 1)
        self.rotatetext = QtWidgets.QLineEdit(self.compframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotatetext.sizePolicy().hasHeightForWidth())
        self.rotatetext.setSizePolicy(sizePolicy)
        self.rotatetext.setMinimumSize(QtCore.QSize(80, 20))
        self.rotatetext.setMaximumSize(QtCore.QSize(70, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        self.rotatetext.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.rotatetext.setFont(font)
        self.rotatetext.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rotatetext.setAutoFillBackground(False)
        self.rotatetext.setDragEnabled(False)
        self.rotatetext.setReadOnly(True)
        self.rotatetext.setObjectName("rotatetext")
        self.gridLayout_2.addWidget(self.rotatetext, 10, 0, 1, 1)
        self.skintext = QtWidgets.QLineEdit(self.compframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.skintext.sizePolicy().hasHeightForWidth())
        self.skintext.setSizePolicy(sizePolicy)
        self.skintext.setMinimumSize(QtCore.QSize(80, 20))
        self.skintext.setMaximumSize(QtCore.QSize(70, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        self.skintext.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.skintext.setFont(font)
        self.skintext.setToolTipDuration(-1)
        self.skintext.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.skintext.setStyleSheet("QLineEdit{ background-color:rgb(30, 30, 30); }")
        self.skintext.setMaxLength(40)
        self.skintext.setFrame(True)
        self.skintext.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.skintext.setCursorPosition(10)
        self.skintext.setDragEnabled(False)
        self.skintext.setReadOnly(True)
        self.skintext.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.skintext.setObjectName("skintext")
        self.gridLayout_2.addWidget(self.skintext, 1, 0, 1, 1)
        self.saturationtext = QtWidgets.QLineEdit(self.compframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saturationtext.sizePolicy().hasHeightForWidth())
        self.saturationtext.setSizePolicy(sizePolicy)
        self.saturationtext.setMinimumSize(QtCore.QSize(80, 20))
        self.saturationtext.setMaximumSize(QtCore.QSize(70, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        self.saturationtext.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.saturationtext.setFont(font)
        self.saturationtext.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.saturationtext.setDragEnabled(False)
        self.saturationtext.setReadOnly(True)
        self.saturationtext.setObjectName("saturationtext")
        self.gridLayout_2.addWidget(self.saturationtext, 17, 0, 1, 1)
        self.sharpnesstext = QtWidgets.QLineEdit(self.compframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sharpnesstext.sizePolicy().hasHeightForWidth())
        self.sharpnesstext.setSizePolicy(sizePolicy)
        self.sharpnesstext.setMinimumSize(QtCore.QSize(80, 20))
        self.sharpnesstext.setMaximumSize(QtCore.QSize(70, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        self.sharpnesstext.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.sharpnesstext.setFont(font)
        self.sharpnesstext.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sharpnesstext.setDragEnabled(False)
        self.sharpnesstext.setReadOnly(True)
        self.sharpnesstext.setObjectName("sharpnesstext")
        self.gridLayout_2.addWidget(self.sharpnesstext, 19, 0, 1, 1)
        self.spottext = QtWidgets.QLineEdit(self.compframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spottext.sizePolicy().hasHeightForWidth())
        self.spottext.setSizePolicy(sizePolicy)
        self.spottext.setMinimumSize(QtCore.QSize(80, 20))
        self.spottext.setMaximumSize(QtCore.QSize(70, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        self.spottext.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.spottext.setFont(font)
        self.spottext.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spottext.setStyleSheet("QLineEdit{ background-color:rgb(30, 30, 30); }")
        self.spottext.setDragEnabled(False)
        self.spottext.setReadOnly(True)
        self.spottext.setObjectName("spottext")
        self.gridLayout_2.addWidget(self.spottext, 3, 0, 1, 1)
        self.sharpness = QtWidgets.QPushButton(self.compframe)
        self.sharpness.setMinimumSize(QtCore.QSize(40, 40))
        self.sharpness.setMaximumSize(QtCore.QSize(40, 40))
        self.sharpness.setStyleSheet("background-color : trasnparent ;\n"
"background : none ;\n"
"border : none;\n"
"background-repeat : none")
        self.sharpness.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("img_532604.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sharpness.setIcon(icon11)
        self.sharpness.setIconSize(QtCore.QSize(40, 40))
        self.sharpness.setObjectName("sharpness")
        self.gridLayout_2.addWidget(self.sharpness, 18, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.rotate = QtWidgets.QPushButton(self.compframe)
        self.rotate.setMinimumSize(QtCore.QSize(40, 40))
        self.rotate.setStyleSheet("background-color : trasnparent ;\n"
"background : none ;\n"
"border : none;\n"
"background-repeat : none\n"
"\n"
"")
        self.rotate.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("rotate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon12.addPixmap(QtGui.QPixmap("rotate.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.rotate.setIcon(icon12)
        self.rotate.setIconSize(QtCore.QSize(40, 40))
        self.rotate.setObjectName("rotate")
        self.gridLayout_2.addWidget(self.rotate, 9, 0, 1, 1)
        self.contrasttext = QtWidgets.QLineEdit(self.compframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contrasttext.sizePolicy().hasHeightForWidth())
        self.contrasttext.setSizePolicy(sizePolicy)
        self.contrasttext.setMinimumSize(QtCore.QSize(80, 20))
        self.contrasttext.setMaximumSize(QtCore.QSize(70, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        self.contrasttext.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.contrasttext.setFont(font)
        self.contrasttext.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.contrasttext.setDragEnabled(False)
        self.contrasttext.setReadOnly(True)
        self.contrasttext.setObjectName("contrasttext")
        self.gridLayout_2.addWidget(self.contrasttext, 12, 0, 1, 1)
        self.skin = QtWidgets.QPushButton(self.compframe)
        self.skin.setMinimumSize(QtCore.QSize(40, 40))
        self.skin.setStyleSheet("background-color : trasnparent ;\n"
"background : none ;\n"
"border : none;\n"
"background-repeat : none\n"
"")
        self.skin.setText("")
        self.skin.setIcon(icon7)
        self.skin.setIconSize(QtCore.QSize(40, 40))
        self.skin.setObjectName("skin")
        self.gridLayout_2.addWidget(self.skin, 0, 0, 1, 1)
        self.brightnesstext = QtWidgets.QLineEdit(self.compframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brightnesstext.sizePolicy().hasHeightForWidth())
        self.brightnesstext.setSizePolicy(sizePolicy)
        self.brightnesstext.setMinimumSize(QtCore.QSize(80, 20))
        self.brightnesstext.setMaximumSize(QtCore.QSize(70, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(230, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 30, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
         
        self.brightnesstext.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.brightnesstext.setFont(font)
        self.brightnesstext.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.brightnesstext.setDragEnabled(False)
        self.brightnesstext.setReadOnly(True)
        self.brightnesstext.setObjectName("brightnesstext")
        self.gridLayout_2.addWidget(self.brightnesstext, 15, 0, 1, 1)
        self.saturation = QtWidgets.QPushButton(self.compframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saturation.sizePolicy().hasHeightForWidth())
        self.saturation.setSizePolicy(sizePolicy)
        self.saturation.setMinimumSize(QtCore.QSize(40, 40))
        self.saturation.setMaximumSize(QtCore.QSize(40, 40))
        self.saturation.setStyleSheet("background-color : trasnparent ;\n"
"background : none ;\n"
"border : none;\n"
"background-repeat : none")
        self.saturation.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("saturation (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saturation.setIcon(icon13)
        self.saturation.setIconSize(QtCore.QSize(40, 40))
        self.saturation.setObjectName("saturation")
        self.gridLayout_2.addWidget(self.saturation, 16, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.facial = QtWidgets.QPushButton(self.compframe)
        self.facial.setMinimumSize(QtCore.QSize(40, 40))
        self.facial.setStyleSheet("background-color : trasnparent ;\n"
"background : none ;\n"
"border : none;\n"
"background-repeat : none\n"
"")
        self.facial.setText("")
        self.facial.setIcon(icon7)
        self.facial.setIconSize(QtCore.QSize(40, 40))
        self.facial.setObjectName("facial")
        self.gridLayout_2.addWidget(self.facial, 4, 0, 1, 1)
        self.rotate.raise_()
        self.skin.raise_()
        self.saturation.raise_()
        self.sharpness.raise_()
        self.spot.raise_()
        self.crop.raise_()
        self.brightness.raise_()
        self.skintext.raise_()
        self.spottext.raise_()
        self.rotatetext.raise_()
        self.brightnesstext.raise_()
        self.contrasttext.raise_()
        self.saturationtext.raise_()
        self.sharpnesstext.raise_()
        self.croptext.raise_()
        self.contrast.raise_()
        self.faciatext.raise_()
        self.facial.raise_()
        self.gridLayout_3.addWidget(self.compframe, 1, 2, 1, 1)
        self.revert = QtWidgets.QPushButton(self.centralwidget)
        self.revert.setMinimumSize(QtCore.QSize(40, 80))
        self.revert.setStyleSheet("background-color : trasnparent ;\n"
"background : none ;\n"
"border : none;\n"
"background-repeat : none")
        self.revert.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.revert.setIcon(icon14)
        self.revert.setIconSize(QtCore.QSize(85, 70))
        self.revert.setAutoRepeatDelay(0)
        self.revert.setAutoRepeatInterval(0)
        self.revert.setObjectName("revert")
        self.gridLayout_3.addWidget(self.revert, 2, 0, 1, 1)
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame.raise_()
        self.revert.raise_()
        self.compframe.raise_()
        fyp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(fyp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1990, 21))
        self.menubar.setObjectName("menubar")
        fyp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(fyp)
        self.statusbar.setObjectName("statusbar")
        fyp.setStatusBar(self.statusbar)

        self.retranslateUi(fyp)
        QtCore.QMetaObject.connectSlotsByName(fyp)
        
         #hiding the buttoons
        self.skin.setHidden(True)
        self.spot.setHidden(True)
        self.rotate.setHidden(True)
        self.crop.setHidden(True)
        self.contrast.setHidden(True)
        self.saturation.setHidden(True)
        self.brightness.setHidden(True)
        self.sharpness.setHidden(True)
        self.saveimg.setHidden(True)
        self.undo.setHidden(True)
        self.redo.setHidden(True)
        self.close.setHidden(True)
        self.cancel.setHidden(True)
        self.apply.setHidden(True)
        self.fix.setHidden(True)
        self.beautify.setHidden(True)
        self.filter.setHidden(True)
        self.facial.setHidden(True)
        #hiding the text fields
        self.skintext.setHidden(True)
        self.spottext.setHidden(True)
        self.rotatetext.setHidden(True)
        self.croptext.setHidden(True)
        self.contrasttext.setHidden(True)
        self.saturationtext.setHidden(True)
        self.brightnesstext.setHidden(True)
        self.sharpnesstext.setHidden(True)
        self.fixtext.setHidden(True)
        self.beautifytext.setHidden(True)
        self.filtertext.setHidden(True)
        self.faciatext.setHidden(True)
        self.slider.setHidden(True)
        
        #writing events on the buttons
        self.filter.clicked.connect(self.beautifyclicked)
        self.beautify.clicked.connect(self.filterclicked)
        self.fix.clicked.connect(self.fixclicked)
        self.contrast.clicked.connect(self.contrastclicked)
        self.sharpness.clicked.connect(self.sharpnessclicked)
        self.brightness.clicked.connect(self.brightnessclicked)
        self.rotate.clicked.connect(self.rotateclicked)
        self.open.clicked.connect(self.openclicked)
        self.saturation.clicked.connect(self.saturationclicked)
        self.saveimg.clicked.connect(self.saveclicked)
        self.cancel.clicked.connect(self.cancelclicked)
        self.apply.clicked.connect(self.applyclicked)
        self.undo.clicked.connect(self.undoclicked)
        self.redo.clicked.connect(self.redoclicked)
        self.skin.clicked.connect(self.skinclicked)
        self.slider.valueChanged.connect(self.valuechange)
        self.revert.clicked.connect(self.revertclicked)
        self.crop.clicked.connect(self.cropclicked)
        self.spot.clicked.connect(self.spotclicked)
        self.facial.clicked.connect(self.facialclicked)

    def retranslateUi(self, fyp):
        _translate = QtCore.QCoreApplication.translate
        fyp.setWindowTitle(_translate("fyp", "Beautify"))
        self.cancel.setText(_translate("fyp", "Cancel"))
        self.apply.setText(_translate("fyp", "Apply"))
        self.filtertext.setText(_translate("fyp", "     Filters"))
        self.fixtext.setText(_translate("fyp", "     Fixes"))
        self.beautifytext.setStyleSheet(_translate("fyp", "QLineEdit{ background-color:rgb(30, 30, 30); }"))
        self.beautifytext.setText(_translate("fyp", "   Beautify"))
        self.croptext.setStyleSheet(_translate("fyp", "QLineEdit{ background-color:rgb(30, 30, 30); }"))
        self.croptext.setText(_translate("fyp", "        Crop"))
        self.faciatext.setText(_translate("fyp", "Facial Retouch"))
        self.rotatetext.setStyleSheet(_translate("fyp", "QLineEdit{ background-color:rgb(30, 30, 30); }"))
        self.rotatetext.setText(_translate("fyp", "       Rotate"))
        self.skintext.setText(_translate("fyp", "Skin Retouch"))
        self.saturationtext.setStyleSheet(_translate("fyp", "QLineEdit{ background-color:rgb(30, 30, 30); }"))
        self.saturationtext.setText(_translate("fyp", "   Saturation"))
        self.sharpnesstext.setStyleSheet(_translate("fyp", "QLineEdit{ background-color:rgb(30, 30, 30); }"))
        self.sharpnesstext.setText(_translate("fyp", "    Sharpness"))
        self.spottext.setText(_translate("fyp", "Spot Removal"))
        self.contrasttext.setStyleSheet(_translate("fyp", "QLineEdit{ background-color:rgb(30, 30, 30); }"))
        self.contrasttext.setText(_translate("fyp", "    Contrast"))
        self.brightnesstext.setStyleSheet(_translate("fyp", "QLineEdit{ background-color:rgb(30, 30, 30); }"))
        self.brightnesstext.setText(_translate("fyp", "   Brightness"))
        
    def valuechange(self):
        factor=20.05
        w=self.image.width()
        h=self.image.height()
        self.concated_temp_path=os.path.join(self.indpath , 'temp_file')+self.typ
        if(self.filter_text=='contrast'):
            print('contrast')
            im = Image.open(self.concated_path)
            enhancer = ImageEnhance.Contrast(im)
            size = self.slider.value()
            self.enhanced_im = enhancer.enhance(1+size/factor)
            self.enhanced_im.save(self.concated_temp_path)
            self.image.setPixmap(QtGui.QPixmap(self.concated_temp_path).scaled(w,h,Qt.KeepAspectRatio))
        elif(self.filter_text=='saturation'):
            print('saturation')
            im = Image.open(self.concated_path)
            enhancer = ImageEnhance.Color(im)
            size = self.slider.value()
            self.enhanced_im = enhancer.enhance(size/factor)
            self.enhanced_im.save(self.concated_temp_path)
            self.image.setPixmap(QtGui.QPixmap(self.concated_temp_path).scaled(w,h,Qt.KeepAspectRatio))
        elif(self.filter_text=='brightness'):
            print('brightness')
            im = Image.open(self.concated_path)
            enhancer = ImageEnhance.Brightness(im)
            size = self.slider.value()
            self.enhanced_im = enhancer.enhance(1+size/factor)
            self.enhanced_im.save(self.concated_temp_path)
            self.image.setPixmap(QtGui.QPixmap(self.concated_temp_path).scaled(w,h,Qt.KeepAspectRatio))
        elif(self.filter_text=='sharpness'):
            print('sharpness')
            im = Image.open(self.concated_path)
            enhancer = ImageEnhance.Sharpness(im)
            size = self.slider.value()
            self.enhanced_im = enhancer.enhance(size/factor)
            self.enhanced_im.save(self.concated_temp_path)
            self.image.setPixmap(QtGui.QPixmap(self.concated_temp_path).scaled(w,h,Qt.KeepAspectRatio))
        size = self.slider.value()
        print(size)
        
    def beautifyclicked(self):
        self.skin.setHidden(False)
        self.spot.setHidden(False)
        self.facial.setHidden(False)
        self.rotate.setHidden(True)
        self.crop.setHidden(True)
        self.contrast.setHidden(True)
        self.saturation.setHidden(True)
        self.brightness.setHidden(True)
        self.sharpness.setHidden(True)
        
        self.skintext.setHidden(False)
        self.spottext.setHidden(False)
        self.faciatext.setHidden(False)
        self.rotatetext.setHidden(True)
        self.croptext.setHidden(True)
        self.contrasttext.setHidden(True)
        self.saturationtext.setHidden(True)
        self.brightnesstext.setHidden(True)
        self.sharpnesstext.setHidden(True)

    
    def filterclicked(self):
        self.skin.setHidden(True)
        self.spot.setHidden(True)
        self.facial.setHidden(True)
        self.rotate.setHidden(True)
        self.crop.setHidden(True)
        self.contrast.setHidden(False)
        self.saturation.setHidden(False)
        self.brightness.setHidden(False)
        self.sharpness.setHidden(False)
        
        self.skintext.setHidden(True)
        self.spottext.setHidden(True)
        self.faciatext.setHidden(True)
        self.rotatetext.setHidden(True)
        self.croptext.setHidden(True)
        self.contrasttext.setHidden(False)
        self.saturationtext.setHidden(False)
        self.brightnesstext.setHidden(False)
        self.sharpnesstext.setHidden(False)
        
    
    def fixclicked(self):
        self.skin.setHidden(True)
        self.spot.setHidden(True)
        self.facial.setHidden(True)
        self.rotate.setHidden(False)
        self.crop.setHidden(False)
        self.contrast.setHidden(True)
        self.saturation.setHidden(True)
        self.brightness.setHidden(True)
        self.sharpness.setHidden(True)
        
        self.skintext.setHidden(True)
        self.spottext.setHidden(True)
        self.faciatext.setHidden(True)
        self.rotatetext.setHidden(False)
        self.croptext.setHidden(False)
        self.contrasttext.setHidden(True)
        self.saturationtext.setHidden(True)
        self.brightnesstext.setHidden(True)
        self.sharpnesstext.setHidden(True)
    
    def contrastclicked(self):
        #creating a temp file to show on label this file would be pverwirtten every time but this will be the source to show on the label
        self.concated_temp_path=os.path.join(self.indpath , 'temp_file')+self.typ
        #setting filter_text for slider valuechange func
        self.slider.setHidden(False)
        self.filter_text='contrast'
        #setting slider value 
        self.slider.setValue(0)
        self.slider.setMinimum(0)
        self.slider.setMaximum(50)
        #setting buttons and textfields
        self.undo.setHidden(True)
        self.redo.setHidden(True)
        self.open.setEnabled(False)
        self.close.setEnabled(False)
        self.saveimg.setEnabled(False)
        self.saturation.setEnabled(False)
        self.brightness.setEnabled(False)
        self.sharpness.setEnabled(False)
        self.beautify.setEnabled(False)
        self.fix.setEnabled(False)
        self.filter.setEnabled(False)
        self.saturationtext.setEnabled(False)
        self.brightnesstext.setEnabled(False)
        self.sharpnesstext.setEnabled(False)
        self.beautifytext.setEnabled(False)
        self.fixtext.setEnabled(False)
        self.filtertext.setEnabled(False)
        self.apply.setHidden(False)
        self.cancel.setHidden(False)
        #save button should appear when there are changes made on the image
        if(self.saveimg.isHidden()==True):
            self.saveimg.setHidden(False)
        self.i=self.i+1
       
    def sharpnessclicked(self):    
         #creating a temp file to show on label this file would be pverwirtten every time but this will be the source to show on the label
        self.concated_temp_path=os.path.join(self.indpath , 'temp_file')+self.typ
        #setting filter_text for slider valuechange func
        self.slider.setHidden(False)
        self.filter_text='sharpness'
        #setting slider value 
        self.slider.setValue(0)
        self.slider.setMinimum(0)
        self.slider.setMaximum(50)
        #setting buttons
        self.undo.setHidden(True)
        self.redo.setHidden(True)
        self.open.setEnabled(False)
        self.close.setEnabled(False)
        self.saveimg.setEnabled(False)
        self.contrast.setEnabled(False)
        self.saturation.setEnabled(False)
        self.brightness.setEnabled(False)
        self.beautify.setEnabled(False)
        self.fix.setEnabled(False)
        self.filter.setEnabled(False)
        self.contrasttext.setEnabled(False)
        self.saturationtext.setEnabled(False)
        self.brightnesstext.setEnabled(False)
        self.beautifytext.setEnabled(False)
        self.fixtext.setEnabled(False)
        self.filtertext.setEnabled(False)
        self.apply.setHidden(False)
        self.cancel.setHidden(False)
        #save button should appear when there are changes made on the image
        if(self.saveimg.isHidden()==True):
            self.saveimg.setHidden(False)
        self.i=self.i+1
    
    def brightnessclicked(self):
         #creating a temp file to show on label this file would be pverwirtten every time but this will be the source to show on the label
        self.concated_temp_path=os.path.join(self.indpath , 'temp_file')+self.typ
        #setting filter_text for slider valuechange func
        self.slider.setHidden(False)
        self.filter_text='brightness'
        #setting slider value 
        self.slider.setValue(0)
        self.slider.setMinimum(0)
        self.slider.setMaximum(50)
        #setting buttons
        self.undo.setHidden(True)
        self.redo.setHidden(True)
        self.open.setEnabled(False)
        self.close.setEnabled(False)
        self.saveimg.setEnabled(False)
        self.contrast.setEnabled(False)
        self.saturation.setEnabled(False)
        self.sharpness.setEnabled(False)
        self.beautify.setEnabled(False)
        self.fix.setEnabled(False)
        self.filter.setEnabled(False)
        self.contrasttext.setEnabled(False)
        self.saturationtext.setEnabled(False)
        self.sharpnesstext.setEnabled(False)
        self.beautifytext.setEnabled(False)
        self.fixtext.setEnabled(False)
        self.filtertext.setEnabled(False)
        self.apply.setHidden(False)
        self.cancel.setHidden(False)
        #save button should appear when there are changes made on the image
        if(self.saveimg.isHidden()==True):
            self.saveimg.setHidden(False)
        self.i=self.i+1
        
    def saturationclicked(self):
         #creating a temp file to show on label this file would be pverwirtten every time but this will be the source to show on the label
        self.concated_temp_path=os.path.join(self.indpath , 'temp_file')+self.typ
        #setting filter_text for slider valuechange func
        self.slider.setHidden(False)
        self.filter_text='saturation'
        #setting slider value 
        self.slider.setValue(0)
        self.slider.setMinimum(0)
        self.slider.setMaximum(50)
        #setting buttons
        self.undo.setHidden(True)
        self.redo.setHidden(True)
        self.open.setEnabled(False)
        self.close.setEnabled(False)
        self.saveimg.setEnabled(False)
        self.contrast.setEnabled(False)
        self.brightness.setEnabled(False)
        self.sharpness.setEnabled(False)
        self.beautify.setEnabled(False)
        self.fix.setEnabled(False)
        self.filter.setEnabled(False)
        self.contrasttext.setEnabled(False)
        self.brightnesstext.setEnabled(False)
        self.sharpnesstext.setEnabled(False)
        self.beautifytext.setEnabled(False)
        self.fixtext.setEnabled(False)
        self.filtertext.setEnabled(False)
        self.apply.setHidden(False)
        self.cancel.setHidden(False)
        #save button should appear when there are changes made on the image
        if(self.saveimg.isHidden()==True):
            self.saveimg.setHidden(False)
        self.i=self.i+1
        
    def rotateclicked(self):
        w=self.image.width()
        h=self.image.height()
         #creating a temp file to show on label this file would be pverwirtten every time but this will be the source to show on the label
        self.concated_temp_path=os.path.join(self.indpath , 'temp_file')+self.typ
        #setting buttons
        self.undo.setHidden(True)
        self.redo.setHidden(True)
        self.open.setEnabled(False)
        self.close.setEnabled(False)
        self.saveimg.setEnabled(False)
        self.crop.setEnabled(False)
        self.beautify.setEnabled(False)
        self.fix.setEnabled(False)
        self.filter.setEnabled(False)
        self.croptext.setEnabled(False)
        self.beautifytext.setEnabled(False)
        self.fixtext.setEnabled(False)
        self.filtertext.setEnabled(False)
        self.apply.setHidden(False)
        self.cancel.setHidden(False)
        #save button should appear when there are changes made on the image
        if(self.saveimg.isHidden()==True):
            self.saveimg.setHidden(False)
        colorImage  = Image.open(self.concated_path)
        self.enhanced_im  = colorImage.rotate(self.rotation_count*-90)
        self.enhanced_im.save(self.concated_temp_path)
        self.image.setPixmap(QtGui.QPixmap(self.concated_temp_path).scaled(w,h,Qt.KeepAspectRatio))
        self.rotation_count=self.rotation_count+1
        if self.rotation_flag==False:
            self.i=self.i+1
        self.rotation_flag=True       
    
    def cropclicked(self):
        w=self.image.width()
        h=self.image.height()
        #creating a temp file to show on label this file would be pverwirtten every time but this will be the source to show on the label
        self.concated_temp_path=os.path.join(self.indpath , 'temp_file')+self.typ
        #setting buttons
        self.undo.setHidden(True)
        self.redo.setHidden(True)
        self.open.setEnabled(False)
        self.close.setEnabled(False)
        self.saveimg.setEnabled(False)
        self.rotate.setEnabled(False)
        self.crop.setEnabled(False)
        self.beautify.setEnabled(False)
        self.fix.setEnabled(False)
        self.filter.setEnabled(False)
        self.rotatetext.setEnabled(False)
        self.croptext.setEnabled(False)
        self.beautifytext.setEnabled(False)
        self.fixtext.setEnabled(False)
        self.filtertext.setEnabled(False)
        self.apply.setHidden(False)
        self.cancel.setHidden(False)
        if(self.saveimg.isHidden()==True):
            self.saveimg.setHidden(False)
        x_start, y_start, x_end, y_end = 0, 0, 0, 0 
        image = cv2.imread(self.concated_path)
        oriImage = image.copy()
        def mouse_crop(event, x, y, flags, param):
            # grab references to the global variables
            global x_start, y_start, x_end, y_end, cropping
            
            # if the left mouse button was DOWN, start RECORDING
            # (x, y) coordinates and indicate that cropping is being
            if event == cv2.EVENT_LBUTTONDOWN:
                x_start, y_start, x_end, y_end = x, y, x, y
                self.cropping = True
                
                # Mouse is Moving
            elif event == cv2.EVENT_MOUSEMOVE:
                if self.cropping == True:
                    x_end, y_end = x, y
                    
                    # if the left mouse button was released
            elif event == cv2.EVENT_LBUTTONUP:
                # record the ending (x, y) coordinates
                x_end, y_end = x, y
                self.cropping = False # cropping is finished
 
                refPoint = [(x_start, y_start), (x_end, y_end)]
            
                if len(refPoint) == 2: #when two points were found
                    roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
                    cv2.imshow("Cropped", roi)
                    cv2.imwrite(self.concated_temp_path,roi)
                    self.image.setPixmap(QtGui.QPixmap(self.concated_temp_path).scaled(w,h,Qt.KeepAspectRatio))
                    self.enhanced_im  = Image.open(self.concated_temp_path)
                    
                
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", mouse_crop)
                
        while True:  
            imgt = image.copy()                   
            if not self.cropping:
                cv2.imshow("image", image)                        
            elif self.cropping:
                cv2.rectangle(imgt, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
                cv2.imshow("image", imgt)   
            k = cv2.waitKey(33)#press 'a'
            if k == -1:  # if no key was pressed, -1 is returned
                continue
            else:
                break                        
            cv2.waitKey(1)
    # close all open windows
        cv2.destroyAllWindows()
        #cropped     = imageObject.crop((xs,ys,xe,ye))
        #Display the cropped portion
        
       # cropped.save(self.concated_temp_path)
        #self.image.setPixmap(QtGui.QPixmap(self.concated_temp_path))
        self.i=self.i+1  
    
    def openclicked(self):
        self.rotation_count=1
        w=self.image.width()
        h=self.image.height()
        print(self.h)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName='string'
        fileName, _ = QFileDialog.getOpenFileName(None,"Open File", "","All Files (*);;Python Files (*.py)", options=options)
        if(fileName != 'string'):
            self.redo.setHidden(True)
            self.undo.setHidden(True)
            img=cv2.imread(fileName)
            #creaeting new directory for temporary usage
            try:  
                os.mkdir(self.indpath)
            except OSError:  
                print ("Creation of the directory %s failed" % self.indpath)
            else:  
                print ("Successfully created the directory %s " % self.indpath)
            self.i=0
            self.maxiter=0
            self.concated_path=os.path.join(self.indpath , 'temp_')+str(self.i)+self.typ
            cv2.imwrite(self.concated_path, img)
            self.image.setPixmap(QtGui.QPixmap(self.concated_path).scaled(w,h,Qt.KeepAspectRatio))
            icon8 = QtGui.QIcon()
            icon8.addPixmap(QtGui.QPixmap(self.concated_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.revert.setIcon(icon8)
            #settign the path to original image in order to retrieve original image
            self.setpath(fileName)
            self.fix.setHidden(False)
            self.beautify.setHidden(False)
            self.filter.setHidden(False)
            self.beautifytext.setHidden(False)
            self.fixtext.setHidden(False)
            self.filtertext.setHidden(False)
            self.close.setHidden(False)

        
    def saveclicked(self):
        filename, _ = QFileDialog.getSaveFileName(None, "Save File", "", ".jpg")
        concat2=filename+".jpg"
        image=cv2.imread(self.concated_path)
        cv2.imwrite(concat2,image)
        
    def revertclicked(self):
        origimg=self.path
        self.image.setPixmap(QtGui.QPixmap(origimg))
        
    def applyclicked(self):
        #setting buttons

        if(self.flag==True):
            self.maxiter=self.i
            print("Yes the flag is true")
            self.flag=False
        self.open.setEnabled(True)
        self.close.setEnabled(True)
        self.saveimg.setEnabled(True)
        self.beautify.setEnabled(True)
        self.fix.setEnabled(True)
        self.filter.setEnabled(True)
        self.beautifytext.setEnabled(True)
        self.fixtext.setEnabled(True)
        self.filtertext.setEnabled(True)
        self.apply.setHidden(True)
        self.cancel.setHidden(True)
        self.undo.setHidden(False)
        self.concated_path=os.path.join(self.indpath , 'temp_')+str(self.i)+self.typ
        self.enhanced_im.save(self.concated_path)
        self.maxiter=self.maxiter+1
        self.rotation_count=1
        self.rotation_flag=False
        if(self.contrast.isHidden()==False):
            self.slider.setHidden(True)
            self.contrast.setEnabled(True)
            self.saturation.setEnabled(True)
            self.brightness.setEnabled(True)
            self.sharpness.setEnabled(True)
            self.contrasttext.setEnabled(True)
            self.saturationtext.setEnabled(True)
            self.brightnesstext.setEnabled(True)
            self.sharpnesstext.setEnabled(True)
        elif(self.rotate.isHidden()==False):
            self.rotate.setEnabled(True)
            self.crop.setEnabled(True)
            self.rotatetext.setEnabled(True)
            self.croptext.setEnabled(True)
        elif(self.skin.isHidden()==False):
            self.skin.setEnabled(True)
            self.spot.setEnabled(True)
            self.skintext.setEnabled(True)
            self.spottext.setEnabled(True)
            self.facial.setEnabled(True)
            self.faciatext.setEnabled(True)
        
    
    def cancelclicked(self):
        w=self.image.width()
        h=self.image.height()
        #setting buttons
        self.beautify.setEnabled(True)
        self.fix.setEnabled(True)
        self.filter.setEnabled(True)
        self.beautifytext.setEnabled(True)
        self.fixtext.setEnabled(True)
        self.filtertext.setEnabled(True)
        self.apply.setHidden(True)
        self.cancel.setHidden(True)
        self.undo.setHidden(True)
        self.rotation_count=1
        self.rotation_flag=False
        if(self.i>self.miniter):
            self.i=self.i-1
        self.concated_path=os.path.join(self.indpath , 'temp_')+str(self.i)+self.typ
        self.enhanced_im = Image.open(self.concated_path)
        self.enhanced_im.save(self.concated_temp_path)
        self.image.setPixmap(QtGui.QPixmap(self.concated_temp_path).scaled(w,h,Qt.KeepAspectRatio))
        self.open.setEnabled(True)
        self.close.setEnabled(True)
        self.saveimg.setEnabled(True)        
        if(self.contrast.isHidden()==False):
            self.slider.setHidden(True)
            self.contrast.setEnabled(True)
            self.saturation.setEnabled(True)
            self.brightness.setEnabled(True)
            self.sharpness.setEnabled(True)
            self.contrasttext.setEnabled(True)
            self.saturationtext.setEnabled(True)
            self.brightnesstext.setEnabled(True)
            self.sharpnesstext.setEnabled(True)
        elif(self.rotate.isHidden()==False):
            self.rotate.setEnabled(True)
            self.crop.setEnabled(True)
            self.rotatetext.setEnabled(True)
            self.croptext.setEnabled(True)
        elif(self.skin.isHidden()==False):
            self.skin.setEnabled(True)
            self.spot.setEnabled(True)
            self.skintext.setEnabled(True)
            self.spottext.setEnabled(True)
            self.facial.setEnabled(True)
            self.faciatext.setEnabled(True)
        
    
    def undoclicked(self):
        w=self.image.width()
        h=self.image.height()
        self.redo.setHidden(False)
        self.redo.setEnabled(True)
        self.flag=True
        if(self.i>self.miniter):
            self.i=self.i-1
            self.concated_path=os.path.join(self.indpath , 'temp_')+str(self.i)+self.typ
            self.enhanced_im = Image.open(self.concated_path)
            self.enhanced_im.save(self.concated_temp_path)
            self.image.setPixmap(QtGui.QPixmap(self.concated_temp_path).scaled(w,h,Qt.KeepAspectRatio))
        elif(self.i<=self.miniter+1):
            self.undo.setEnabled(False)
            self.redo.setEnabled(True)
    
    def redoclicked(self):
        w=self.image.width()
        h=self.image.height()
        if(self.i<=self.maxiter-1):
            self.undo.setEnabled(True)
            self.i=self.i+1
            self.concated_path=os.path.join(self.indpath , 'temp_')+str(self.i)+self.typ
            self.enhanced_im = Image.open(self.concated_path)
            self.enhanced_im.save(self.concated_temp_path)
            self.image.setPixmap(QtGui.QPixmap(self.concated_temp_path).scaled(w,h,Qt.KeepAspectRatio))
        elif(self.i>self.maxiter-1):
            self.redo.setEnabled(False)
    
    def skinclicked(self):
        self.skin.setEnabled(False)
        self.spot.setEnabled(False)
        self.beautify.setEnabled(False)
        self.fix.setEnabled(False)
        self.filter.setEnabled(False)
        self.facial.setEnabled(False)
        self.skintext.setEnabled(False)
        self.spottext.setEnabled(False)
        self.beautifytext.setEnabled(False)
        self.fixtext.setEnabled(False)
        self.filtertext.setEnabled(False)
        self.faciatext.setEnabled(False)
        self.open.setEnabled(False)
        self.close.setEnabled(False)
        self.saveimg.setEnabled(False)
        
        
        self.concated_path=os.path.join(self.indpath , 'temp_')+str(self.i)+self.typ
        cp=os.path.join(self.indpath , 'imagecroped')+self.typ
        self.ApplyToImage(self.concated_path, True)
        
        self.blurimage(self.concated_path)
        
        cp=os.path.join(self.indpath , 'skindetect')+self.typ
        cp2=os.path.join(self.indpath , 'blurred')+self.typ
        self.skin_blurred_orignal(cp,self.concated_path,cp2)
        self.orig_and_blurred(self.concated_path,cp2)
                
        cp=os.path.join(self.indpath , 'skindetect')+self.typ
        cp2=os.path.join(self.indpath , 'orig_with_blurred')+self.typ
        cp3=os.path.join(self.indpath , 'nonskindetect')+self.typ
        self.final_result(cp2,cp,cp3)
        self.apply.setHidden(False)
        self.cancel.setHidden(False)
        self.i=self.i+1
              
        
        
        
    def spotclicked(self):
        self.skin.setEnabled(False)
        self.spot.setEnabled(False)
        self.beautify.setEnabled(False)
        self.fix.setEnabled(False)
        self.filter.setEnabled(False)
        self.facial.setEnabled(False)
        self.skintext.setEnabled(False)
        self.spottext.setEnabled(False)
        self.beautifytext.setEnabled(False)
        self.fixtext.setEnabled(False)
        self.filtertext.setEnabled(False)
        self.faciatext.setEnabled(False)
        self.open.setEnabled(False)
        self.close.setEnabled(False)
        self.saveimg.setEnabled(False)
        
        self.spotdetect(self.concated_path)
        cp=os.path.join(self.indpath , 'crop_spot')+self.typ
        self.mask_creation(cp)
        cp=os.path.join(self.indpath , 'mask_of_spot')+self.typ
        self.heal_spot(cp,self.concated_path)
        self.apply.setHidden(False)
        self.cancel.setHidden(False)
        self.i=self.i+1
        
    def ApplyToImage(self,path, flUseHSVColorspace):
       data, labels= self.ReadData()
       clf= self.TrainTree(data, labels, flUseHSVColorspace)
       img= cv2.imread(path)
       cv2.imshow('image', img) 
    # Wait for a key 
       while(True):
           k = cv2.waitKey(33)#press 'a'
           if k == -1:  # if no key was pressed, -1 is returned
               continue
           else:
               break
        #cv2.destroyWindow('Original Image') 
       cv2.destroyWindow('image')
       print(img.shape)
       data= np.reshape(img,(img.shape[0]*img.shape[1],3))
       print(data.shape)
       if(flUseHSVColorspace):
           data= self.BGR2HSV(data)
           predictedLabels= clf.predict(data)
           imgLabels= np.reshape(predictedLabels,(img.shape[0],img.shape[1],1))
       if (flUseHSVColorspace):
           self.concated_path_2=os.path.join(self.indpath , 'skindetect')+self.typ
           cv2.imwrite(self.concated_path_2,((-(imgLabels-1)+1)*255))# from [1 2] to [0 255]
           cv2.imshow('skin detected', ((-(imgLabels-1)+1)*255)) 
           # Wait for a key 
           while(True):
               k = cv2.waitKey(33)#press 'a'
               if k == -1:  # if no key was pressed, -1 is returned
                   continue
               else:
                   break
        #cv2.destroyWindow('Original Image') 
           cv2.destroyWindow('skin detected')
       else:
           self.concated_path_2=os.path.join(self.indpath , 'skindetect')+self.typ
           cv2.imwrite(self.concated_path_2,((-(imgLabels-1)+1)*255))
    
    def BGR2HSV(self,bgr):
        bgr= np.reshape(bgr,(bgr.shape[0],1,3))
        hsv= cv2.cvtColor(np.uint8(bgr), cv2.COLOR_BGR2HSV)
        hsv= np.reshape(hsv,(hsv.shape[0],3))
        return hsv
    
    def TrainTree(self,data, labels, flUseHSVColorspace):
        if(flUseHSVColorspace):
            data= self.BGR2HSV(data)
        trainData, testData, trainLabels, testLabels = train_test_split(data, labels, test_size=0.20, random_state=42)
        print(trainData.shape)
        print(trainLabels.shape)
        print(testData.shape)
        print(testLabels.shape)
        clf = tree.DecisionTreeClassifier(criterion='entropy')
        clf = clf.fit(trainData, trainLabels)
        print(clf.feature_importances_)
        print(clf.score(testData, testLabels))
        return clf
    
    def ReadData(self):
    #Data in format [B G R Label] from
        data = np.genfromtxt('D:/skin_nonskin.txt', dtype=np.int32)
        labels= data[:,3]
        data= data[:,0:3]
        return data, labels
    
    def orig_and_blurred(self,org,blurd):
        origimg=cv2.imread(org)
        blurred=cv2.imread(blurd)
        img = cv2.addWeighted(origimg, 0.5, blurred, 0.5, 0)
        self.concated_path_2=os.path.join(self.indpath , 'orig_with_blurred')+self.typ
        cv2.imshow('original and blurred', img) 
           # Wait for a key 
        while(True):
            k = cv2.waitKey(33)#press 'a'
            if k == -1:  # if no key was pressed, -1 is returned
                continue
            else:
                break
        #cv2.destroyWindow('Original Image') 
        cv2.destroyWindow('original and blurred')
        cv2.imwrite(self.concated_path_2,img)
        
    def facedetect(self,image):
        facedet=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
        if facedet.empty():
            print("not successful")
        im = cv2.imread(image)
        height = im.shape[0]
        width = im.shape[1]
        crop_img = np.zeros((height,width,3), np.uint8)
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces = facedet.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
        for(x,y,w,h) in faces:
            crop_img[y:y+h+30, x:x+w] = im[y:y+h+30, x:x+w]
            self.concated_path_2=os.path.join(self.indpath , 'imagecroped')+self.typ
            cv2.imwrite(self.concated_path_2,crop_img)
            cv2.imshow("cropped face", crop_img)
            while(True):
                k = cv2.waitKey(33)#press 'a'
                if k == -1:  # if no key was pressed, -1 is returned
                    continue
                else:
                    break
            cv2.destroyWindow('cropped face')
        return faces
        
    def skin_blurred_orignal(self,mask,orig,blur):
        skin= cv2.imread(mask)
        orgimg=cv2.imread(orig)
        blurred=cv2.imread(blur)
        bitandskin=cv2.bitwise_and(skin,orgimg)
        bitandblur=cv2.bitwise_and(skin,blurred)
        nonskin=cv2.subtract(orgimg,bitandskin)
        self.concated_path_2=os.path.join(self.indpath , 'nonskindetect')+self.typ
        cv2.imwrite(self.concated_path_2,nonskin)
        cv2.imshow('Non skin',nonskin) 
           # Wait for a key 
        while(True):
            k = cv2.waitKey(33)#press 'a'
            if k == -1:  # if no key was pressed, -1 is returned
                continue
            else:
                break
        #cv2.destroyWindow('Original Image') 
        cv2.destroyWindow('Non skin')          
        self.concated_path_2=os.path.join(self.indpath , 'skinand')+self.typ
        cv2.imwrite(self.concated_path_2,bitandskin)
        cv2.imshow('Bit AND of skin mask and orignal image', bitandskin)
           # Wait for a key 
        while(True):
            k = cv2.waitKey(33)#press 'a'
            if k == -1:  # if no key was pressed, -1 is returned
                continue
            else:
                break
        #cv2.destroyWindow('Original Image') 
        cv2.destroyWindow('Bit AND of skin mask and orignal image')     
        self.concated_path_2=os.path.join(self.indpath , 'blurredand')+self.typ
        cv2.imwrite(self.concated_path_2,bitandblur)
        cv2.imshow('Bit AND of skin mask and blurred image', bitandblur)
           # Wait for a key 
        while(True):
            k = cv2.waitKey(33)#press 'a'
            if k == -1:  # if no key was pressed, -1 is returned
                continue
            else:
                break
        #cv2.destroyWindow('Original Image') 
        cv2.destroyWindow('Bit AND of skin mask and blurred image')
        
    def blurimage(self,path):
        origimg=cv2.imread(path)
        #kernel_19x19 = np.ones((19,19), np.float32)/361
        blurred2 =cv2.bilateralFilter(origimg, 150,70, 400)
        self.concated_path_2=os.path.join(self.indpath , 'blurred')+self.typ
        cv2.imwrite(self.concated_path_2,blurred2)
        cv2.imshow('Blurred image', blurred2)
           # Wait for a key 
        while(True):
            k = cv2.waitKey(33)#press 'a'
            if k == -1:  # if no key was pressed, -1 is returned
                continue
            else:
                break
        #cv2.destroyWindow('Original Image') 
        cv2.destroyWindow('Blurred4 image')
    
    def final_result(self,org,skn,non):
        w=self.image.width()
        h=self.image.height()
        self.concated_temp_path=os.path.join(self.indpath , 'temp_file')+self.typ
        origblur=cv2.imread(org)
        skin=cv2.imread(skn)
        nonskin=cv2.imread(non)
        bitandorgblurskin=cv2.bitwise_and(skin,origblur)
        final_img=bitandorgblurskin+nonskin
        cv2.imwrite(self.concated_temp_path,final_img)
        self.image.setPixmap(QtGui.QPixmap(self.concated_temp_path).scaled(w,h,Qt.KeepAspectRatio))
        self.enhanced_im  = Image.open(self.concated_temp_path)
        cv2.imshow('Bit AND of skin mask and Blurred image then adding with non skin', final_img)
        cv2.imshow('bitandorg',bitandorgblurskin)
           # Wait for a key 
        while(True):
            k = cv2.waitKey(33)#press 'a'
            if k == -1:  # if no key was pressed, -1 is returned
                continue
            else:
                break
        #cv2.destroyWindow('Original Image') 
        cv2.destroyWindow('Bit AND of skin mask and Blurred image then adding with non skin')
        cv2.destroyWindow('bitandorg')
    
    def spotdetect(self,imgpath):
        MODEL_NAME = 'inference_graph'
        IMAGE_NAME = imgpath

        # Grab path to current working directory
        CWD_PATH = 'C:/tensorflow1/models/research/object_detection'
        
        # Path to frozen detection graph .pb file, which contains the model that is used
        # for object detection.
        PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')
        
        # Path to label map file
        PATH_TO_LABELS = os.path.join(CWD_PATH,'training','labelmap.pbtxt')
        
        # Path to image
        PATH_TO_IMAGE = os.path.join(CWD_PATH,IMAGE_NAME)
        
        # Number of classes the object detector can identify
        NUM_CLASSES = 1
            
        # Load the label map.
        # Label maps map indices to category names, so that when our convolution
        # network predicts `5`, we know that this corresponds to `king`.
        # Here we use internal utility functions, but anything that returns a
        # dictionary mapping integers to appropriate string labels would be fine
        label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
        categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
        category_index = label_map_util.create_category_index(categories)
        
        # Load the Tensorflow model into memory.
        detection_graph = tf.Graph()
        with detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')
            sess = tf.Session(graph=detection_graph)
        
        #    Define input and output tensors (i.e. data) for the object detection classifier
        
        # Input tensor is the image
        image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
        
        # Output tensors are the detection boxes, scores, and classes
        # Each box represents a part of the image where a particular object was detected
        detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
        
        # Each score represents level of confidence for each of the objects.
        # The score is shown on the result image, together with the class label.
        detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
        detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
        
        # Number of objects detected
        num_detections = detection_graph.get_tensor_by_name('num_detections:0')
        
        # Load image using OpenCV and
        # expand image dimensions to have shape: [1, None, None, 3]
        # i.e. a single-column array, where each item in the column has the pixel RGB value
        image = cv2.imread(PATH_TO_IMAGE)
        image_expanded = np.expand_dims(image, axis=0)
        
        # Perform the actual detection by running the model with the image as input
        (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores, detection_classes, num_detections],
                feed_dict={image_tensor: image_expanded})
        
        # Draw the results of the detection (aka 'visulaize the results')
        
        vis_util.visualize_boxes_and_labels_on_image_array(
                image,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=8,
                min_score_thresh=0.6)
        
        final_score = np.squeeze(scores)    
        count = 0
        for i in range(100):
            if scores is None or final_score[i] > 0.5:
                count = count + 1
        im = cv2.imread(IMAGE_NAME)
        imcopy=im.copy()
        height = im.shape[0]
        width = im.shape[1]
        crop_img = np.zeros((height,width,3), np.uint8)
        for i in range(count):
            crop_img[int(boxes[0][i][0]*height):int(boxes[0][i][2]*height),int(boxes[0][i][1]*width):int(boxes[0][i][3]*width)] = im[int(boxes[0][i][0]*height):int(boxes[0][i][2]*height),int(boxes[0][i][1]*width):int(boxes[0][i][3]*width)]
            #im[int(boxes[0][i][0]*height):int(boxes[0][i][2]*height),int(boxes[0][i][1]*width):int(boxes[0][i][3]*width)]= im[int((boxes[0][i][0]*height)-1),int((boxes[0][i][1]*width)):int(boxes[0][i][3]*width)]
            #print(int((boxes[0][i][0]*height)-1))
            
            #crop_img[int(boxes[0][0][0]*height):int(boxes[0][0][2]*height),int(boxes[0][0][1]*width):int(boxes[0][0][3]*width)] = im[int(boxes[0][0][0]*height):int(boxes[0][0][2]*height),int(boxes[0][0][1]*width):int(boxes[0][0][3]*width)]
            # All the results have been drawn on image. Now display the image.
        self.concated_path_2=os.path.join(self.indpath , 'spot_detected')+self.typ
        cv2.imwrite(self.concated_path_2,image)
        cv2.imshow('Object detector', image)
        cv2.imshow('cropped image',crop_img)
        skinnospot=cv2.subtract(imcopy,crop_img)
        cv2.imshow('no spot image',skinnospot)
        
        # Press any key to close the image
        cv2.waitKey(0)
        
        # Clean up
        cv2.destroyAllWindows()
        self.concated_path_2=os.path.join(self.indpath , 'crop_spot')+self.typ
        cv2.imwrite(self.concated_path_2,crop_img)
        self.concated_path_2=os.path.join(self.indpath , 'no_spot')+self.typ
        cv2.imwrite(self.concated_path_2,skinnospot)
        

    def mask_creation(self,img):
        mask=cv2.imread(img)
        grayImage = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 0, 255, cv2.THRESH_BINARY)
        cv2.imshow('mask', blackAndWhiteImage)
        while(True):
            k = cv2.waitKey(33)#press 'a'
            if k == -1:  # if no key was pressed, -1 is returned
                continue
            else:
                break
            #cv2.destroyWindow('Original Image') 
        cv2.destroyWindow('mask')
        self.concated_path_2=os.path.join(self.indpath , 'mask_of_spot')+self.typ
        cv2.imwrite(self.concated_path_2,blackAndWhiteImage)
        
    def heal_spot(self,msk,org):
        w=self.image.width()
        h=self.image.height()
        self.concated_temp_path=os.path.join(self.indpath , 'temp_file')+self.typ
        mask=cv2.imread(msk,0)
        orig=cv2.imread(org)
        spot_healed = cv2.inpaint(orig,mask,3,cv2.INPAINT_TELEA)
        cv2.imshow('dst',spot_healed)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite(self.concated_temp_path,spot_healed)
        self.image.setPixmap(QtGui.QPixmap(self.concated_temp_path).scaled(w,h,Qt.KeepAspectRatio))
        self.enhanced_im  = Image.open(self.concated_temp_path)
        
    def facialclicked(self):
        self.skin.setEnabled(False)
        self.spot.setEnabled(False)
        self.beautify.setEnabled(False)
        self.fix.setEnabled(False)
        self.filter.setEnabled(False)
        self.facial.setEnabled(False)
        self.skintext.setEnabled(False)
        self.spottext.setEnabled(False)
        self.beautifytext.setEnabled(False)
        self.fixtext.setEnabled(False)
        self.filtertext.setEnabled(False)
        self.faciatext.setEnabled(False)
        self.open.setEnabled(False)
        self.close.setEnabled(False)
        self.saveimg.setEnabled(False)
        
        
        self.concated_path=os.path.join(self.indpath , 'temp_')+str(self.i)+self.typ
        face=self.facedetect(self.concated_path)
        try:
            if(face.any()==True):
                cp=os.path.join(self.indpath , 'imagecroped')+self.typ
                self.ApplyToImage(cp, True)
                
                self.blurimage(self.concated_path)
                
                cp=os.path.join(self.indpath , 'skindetect')+self.typ
                cp2=os.path.join(self.indpath , 'blurred')+self.typ
                self.skin_blurred_orignal(cp,self.concated_path,cp2)
                self.orig_and_blurred(self.concated_path,cp2)
                
                cp=os.path.join(self.indpath , 'skindetect')+self.typ
                cp2=os.path.join(self.indpath , 'orig_with_blurred')+self.typ
                cp3=os.path.join(self.indpath , 'nonskindetect')+self.typ
                self.final_result(cp2,cp,cp3)
                self.apply.setHidden(False)
                self.cancel.setHidden(False)
                self.i=self.i+1
                
        except:
           ctypes.windll.user32.MessageBoxW(0, "No face was detected in the Image. Please use Skin Retouching instead of Facial Retouching", "Face Detection Failed", 1)
           self.skin.setEnabled(True)
           self.spot.setEnabled(True)
           self.beautify.setEnabled(True)
           self.fix.setEnabled(True)
           self.filter.setEnabled(True)
           self.facial.setEnabled(True)
           self.skintext.setEnabled(True)
           self.spottext.setEnabled(True)
           self.beautifytext.setEnabled(True)
           self.fixtext.setEnabled(True)
           self.filtertext.setEnabled(True)
           self.faciatext.setEnabled(True)
           self.open.setEnabled(True)
           self.close.setEnabled(True)
           self.saveimg.setEnabled(True)
#funcrion to save original path of image in order to reser all changes
        
    def setpath(self,filename):
        self.path=filename


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fyp = QtWidgets.QMainWindow()
    ui = Ui_fyp()
    ui.setupUi(fyp)
    fyp.show()
    sys.exit(app.exec_())

