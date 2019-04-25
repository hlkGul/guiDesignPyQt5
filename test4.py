# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QImage, QPainter, QPalette, QPixmap
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QLabel,
        QMainWindow, QMenu, QMessageBox, QScrollArea, QSizePolicy)
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter

class Ui_guiTemplate(object):

    def setupUi(self, guiTemplate):
        guiTemplate.setObjectName("guiTemplate")
        guiTemplate.resize(980, 735)
        self.centralwidget = QtWidgets.QWidget(guiTemplate)
        self.centralwidget.setObjectName("centralwidget")
        # self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        # self.gridLayout.setObjectName("gridLayout")      
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 585, 100))
        self.tabWidget.setObjectName("tabWidget")
        #self.tabWidget.setCurrentWidget(self.ımagesTab)
        self.Common = QtWidgets.QWidget()
        self.Common.setObjectName("Common")
        #self.Common.setToolTip("Common Features")
        self.tabWidget.addTab(self.Common, "")
        #self.tabWidget.setCornerWidget(self.Common, QtCore.Qt.TopRightCorner)


        self.Data = QtWidgets.QWidget()
        self.Data.setObjectName("Data")
        self.tabWidget.addTab(self.Data, "")
        #self.Data.setToolTip("Data Features")
     
        self.Devices = QtWidgets.QWidget()
        self.Devices.setObjectName("Devices")
        self.tabWidget.addTab(self.Devices, "")
        #self.Devices.setToolTip("Devices Features")
      
        self.Filter = QtWidgets.QWidget()
        self.Filter.setObjectName("Filter")
        self.tabWidget.addTab(self.Filter, "")
        #self.Filter.setToolTip("Filters Features")
      
        self.Images = QtWidgets.QWidget()
        self.Images.setObjectName("Images")
        self.tabWidget.addTab(self.Images, "")
        self.ımagesTab()
        #self.Images.setToolTip("Images Features")
      
        self.Transform = QtWidgets.QWidget()
        self.Transform.setObjectName("Transform")
        self.tabWidget.addTab(self.Transform, "")
        self.transformTab()
        #self.Transform.setToolTip("Transform Features")
     
        self.ProgramExecution = QtWidgets.QWidget()
        self.ProgramExecution.setObjectName("ProgramExecution")
        self.tabWidget.addTab(self.ProgramExecution, "")
        #self.ProgramExecution.setToolTip("Program Exec. Features")
        
        # self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 5)
    
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(300, 99, 271, 241))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        # self.gridLayout.addWidget(self.frame, 1, 3, 2, 1)
      

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(600, 500, 256, 192))
        self.graphicsView.setObjectName("graphicsView")
        # self.gridLayout.addWidget(self.graphicsView, 3, 4, 1, 2)

        self.menuBarFun()
        self.controlButtons()
        self.scrollAreaFun()
        self.toolBoxFun()

        guiTemplate.setCentralWidget(self.centralwidget)

        #status bar is visible bottom of the page
        self.statusbar = QtWidgets.QStatusBar(guiTemplate)
        self.statusbar.setObjectName("statusbar")
        guiTemplate.setStatusBar(self.statusbar)
        #self.centralwidget.setWidgetResizable(True)
        self.retranslateUi(guiTemplate)
        self.tabWidget.setCurrentIndex(2)

        self.Tools.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(guiTemplate)

    def toolBoxFun(self):   

        self.Tools = QtWidgets.QToolBox(self.centralwidget)
        self.Tools.setGeometry(QtCore.QRect(720, 100, 250, 391))
        self.Tools.setObjectName("Tools")         
    
        #self.toolsLayout = QtWidgets.QGridLayout()
        self.imageNavGroupBox = QtWidgets.QGroupBox()
        self.mainLayoutTools = QtWidgets.QVBoxLayout()
        self.mainLayoutTools.addWidget(self.imageNavGroupBox)
        gridLayImNAv = QtWidgets.QGridLayout(self.imageNavGroupBox)
        gridLayImNAv.setAlignment(QtCore.Qt.AlignTop)
        gridLayImNAv.addWidget(QtWidgets.QLabel('Region'),0,0)
        gridLayImNAv.addWidget(QtWidgets.QLabel('Image Memory'),1,0)
        gridLayImNAv.addWidget(QtWidgets.QLabel('Resolution'),2,0)
        gridLayImNAv.addWidget(QtWidgets.QLabel('Format'),3,0)
        gridLayImNAv.addWidget(QtWidgets.QLabel('Caption'),4,0)
        gridLayImNAv.addWidget(QtWidgets.QComboBox(),0,1)
        gridLayImNAv.addWidget(QtWidgets.QComboBox(),1,1)
        gridLayImNAv.addWidget(QtWidgets.QComboBox(),2,1)
        gridLayImNAv.addWidget(QtWidgets.QComboBox(),3,1)
        gridLayImNAv.addWidget(QtWidgets.QComboBox(),4,1)
        
        self.pixInfoGroup = QtWidgets.QGroupBox()
        self.mainlayPixInf =QtWidgets.QVBoxLayout()
        self.mainlayPixInf.addWidget(self.pixInfoGroup)
        gridPixInf = QtWidgets.QGridLayout(self.pixInfoGroup)
        gridPixInf.setAlignment(QtCore.Qt.AlignTop)
        gridPixInf.addWidget(QtWidgets.QLabel('world'),0,0)
        gridPixInf.addWidget(QtWidgets.QLabel('image'),1,0)
        gridPixInf.addWidget(QtWidgets.QLabel('pixel value'),2,0)

        self.Tools.addItem(self.imageNavGroupBox, "")
        self.Tools.addItem(self.pixInfoGroup,"")
      
        # self.imagenavigator = QtWidgets.QWidget()
        # self.imagenavigator.setGeometry(QtCore.QRect(0, 0, 131, 337))
        # self.imagenavigator.setMouseTracking(False)
        # self.imagenavigator.setObjectName("imagenavigator")
        # self.Tools.addItem(self.imagenavigator, "")
      
        # self.pixelinfo = QtWidgets.QWidget()
        # self.pixelinfo.setGeometry(QtCore.QRect(0, 0, 131, 337))
        # self.pixelinfo.setObjectName("pixelinfo")
        # self.Tools.addItem(self.pixelinfo, "")
        #self.Tools.setCurrentWidget(self.pixelinfo)

        # self.gridLayout.addWidget(self.Tools, 1, 5, 2, 1)        

    def scrollAreaFun(self):
        self.imageMemory = QtWidgets.QScrollArea(self.centralwidget)
        self.imageMemory.setGeometry(QtCore.QRect(590, 100, 120, 291))
        self.imageMemory.setMouseTracking(True)
        self.imageMemory.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.imageMemory.setWidgetResizable(True)
        self.imageMemory.setObjectName("imageMemory")
        #self.imageMemory.setAlignment(QtCore.Qt.AlignTop)
        self.imageMemory.setBackgroundRole(QPalette.Light)
        self.imageMemory.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        self.scrollLayout = QtWidgets.QVBoxLayout(self.imageMemory)
        self.scrollLayout.setAlignment(Qt.AlignTop|Qt.AlignJustify)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 118, 289))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        self.im0 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.im0.setText("Im 0")
        self.im0.setStyleSheet("border:1px") 

        self.im1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.im1.setText("Im 1")
        self.im1.setStyleSheet("border:1px")
   
        self.im2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.im2.setText("Im 2")
        self.im2.setStyleSheet("border:1px") 

        self.im3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.im3.setText("Im 3")
        self.im3.setStyleSheet("border:1px") 

        self.im4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.im4.setText("Im 4")
        self.im4.setStyleSheet("border:1px") 

        if self.im0.pressed:
            self.im0.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))")
        elif self.im0.disabled:
            self.im0.setStyleSheet("background-color: rgb(170, 170, 127)")
        else:
            self.im0.setStyleSheet("background-color: #3cbaa2; border: 1px solid black; border-radius: 5px") 
                  
        if self.im1.pressed:
            self.im1.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))")
        elif self.im1.disabled:
            self.im1.setStyleSheet("background-color: rgb(170, 170, 127)")
        else:
            self.im1.setStyleSheet("background-color: #3cbaa2; border: 1px solid black; border-radius: 5px") 
    
        if self.im2.pressed:
            self.im2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))")
        elif self.im2.disabled:
            self.im2.setStyleSheet("background-color: rgb(170, 170, 127)")
        else:
            self.im2.setStyleSheet("background-color: #3cbaa2; border: 1px solid black; border-radius: 5px") 

        if self.im3.pressed:
            self.im3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))")
        elif self.im3.disabled:
            self.im3.setStyleSheet("background-color: rgb(170, 170, 127)")
        else:
            self.im3.setStyleSheet("background-color: #3cbaa2; border: 1px solid black; border-radius: 5px")             

        if self.im4.pressed:
            self.im4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   stop:0 rgba(60, 186, 162, 255), stop:1 rgba(98, 211, 162, 255))")
        elif self.im4.disabled:
            self.im4.setStyleSheet("background-color: rgb(170, 170, 127)")
        else:
            self.im4.setStyleSheet("background-color: #3cbaa2; border: 1px solid black; border-radius: 5px") 

        self.scrollLayout.addWidget(self.im0)
        self.scrollLayout.addWidget(self.im1)
        self.scrollLayout.addWidget(self.im2)
        self.scrollLayout.addWidget(self.im3)
        self.scrollLayout.addWidget(self.im4)

       
        #self.centralwidget.setLayout(scrollLayout)  
        # self.gridLayout.addWidget(self.imageMemory, 1, 4, 1, 1)

    def menuBarFun(self):    
        self.menubar = QtWidgets.QMenuBar(guiTemplate)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 861, 21))
       
       #File menus actions
        self.exitAct = QtWidgets.QAction(QtGui.QIcon('exitt.png'),'&Exit',self.centralwidget)
        self.exitAct.triggered.connect(QtWidgets.qApp.quit)
        self.newAct = QtWidgets.QAction(QtGui.QIcon('new-file.png'),'&New',self.centralwidget)
        self.openAct = QtWidgets.QAction(QtGui.QIcon('open-folder-outline'),'&Open',self.centralwidget)
        self.saveAct = QtWidgets.QAction(QtGui.QIcon('save.png'),'&Save',self.centralwidget)
        self.loadAct = QtWidgets.QAction(QtGui.QIcon('spinner-of-dots'),'&Load Image',self.centralwidget)
        self.saveImAct = QtWidgets.QAction(QtGui.QIcon('picture.png'),'&Save Image',self.centralwidget)
        self.loginAct = QtWidgets.QAction(QtGui.QIcon('log-in.png'),'&Log in',self.centralwidget)
        self.logoutAct = QtWidgets.QAction(QtGui.QIcon('logout.png'),'&Log out',self.centralwidget)

        #settings menus actions
        self.environmentAct = QtWidgets.QAction(QtGui.QIcon('vegetables.png'),'&Environment',self.centralwidget)
        self.inspectionAct = QtWidgets.QAction(QtGui.QIcon('inspection.png'),'&Inspection',self.centralwidget)
        self.managementAct = QtWidgets.QAction(QtGui.QIcon('management.png'),'&Management',self.centralwidget)
        self.optionsAct = QtWidgets.QAction(QtGui.QIcon('settings-work-tool.png'),'&Options',self.centralwidget)

        #help menu actions
        self.showHelpAct = QtWidgets.QAction(QtGui.QIcon('information.png'),'&Show Help',self.centralwidget)
        self.aboutGuiAct = QtWidgets.QAction(QtGui.QIcon('instruction.png'),'&About Gui',self.centralwidget)


        self.menubar.setObjectName("menubar")
        self.fileMenu = self.menubar.addMenu('&File')
        self.settingsMenu = self.menubar.addMenu('&Settings')
        self.diagnosisMEnu = self.menubar.addMenu('&Diagnosis')
        self.helpMenu = self.menubar.addMenu('&Help')

        #file actions adding
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)          
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.loadAct)          
        self.fileMenu.addAction(self.saveImAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.loginAct)          
        self.fileMenu.addAction(self.logoutAct) 
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)       

        #settings actions adding
        self.settingsMenu.addAction(self.environmentAct)
        self.settingsMenu.addAction(self.inspectionAct)
        self.settingsMenu.addAction(self.managementAct)
        self.settingsMenu.addAction(self.optionsAct)

        #help actions adding
        self.helpMenu.addAction(self.showHelpAct)
        self.helpMenu.addAction(self.aboutGuiAct)

        #add menus to gui
        guiTemplate.setMenuBar(self.menubar)
  
    def controlButtons(self):
       
        self.mainLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.mainLayoutWidget.setGeometry(QtCore.QRect(10,95,520,50))
        self.mainLayoutWidget.setObjectName("control buttons widget")
        self.mainLayoutButtons = QtWidgets.QHBoxLayout(self.mainLayoutWidget)
        self.mainLayoutButtons.setAlignment(QtCore.Qt.AlignLeft)
        self.mainLayoutButtons.setContentsMargins(0,0,0,0)
        self.mainLayoutButtons.setObjectName("control buttons alignment")

        self.play = QtWidgets.QToolButton(self.mainLayoutWidget)
        #self.play.setGeometry(QtCore.QRect(10, 100, 75, 23))
        self.play.setObjectName("")
        self.play.setIcon(QtGui.QIcon('play-button.png'))
        self.play.setIconSize(QtCore.QSize(20,20))
        self.play.setStyleSheet("border:1px ")
        self.play.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.play.setToolTip("Start Acquisition")

        self.pushButton_2 = QtWidgets.QToolButton(self.mainLayoutWidget)
        #self.pushButton_2.setGeometry(QtCore.QRect(60, 100, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setIcon(QtGui.QIcon('pause.png'))
        self.pushButton_2.setIconSize(QtCore.QSize(20,20))
        self.pushButton_2.setStyleSheet("border:1px ")
        self.pushButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.pushButton_2.setToolTip("Pause Acquisition")

    
        self.pushButton_3 = QtWidgets.QToolButton(self.mainLayoutWidget)
        #self.pushButton_3.setGeometry(QtCore.QRect(110, 100, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setIcon(QtGui.QIcon('stop.png'))
        self.pushButton_3.setIconSize(QtCore.QSize(20,20))
        self.pushButton_3.setStyleSheet("border:1px")
        self.pushButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.pushButton_3.setToolTip("Stop Acquisition")


        self.openCamera = QtWidgets.QToolButton(self.mainLayoutWidget)
        #self.openCamera.setGeometry(QtCore.QRect(160, 100, 75, 23))
        self.openCamera.setObjectName("")
        self.openCamera.setIcon(QtGui.QIcon('shutter-open.png'))
        self.openCamera.setIconSize(QtCore.QSize(20,20))
        self.openCamera.setStyleSheet("border:1px ")
        self.openCamera.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.openCamera.setToolTip("Open Camera")


        self.closeCamera = QtWidgets.QToolButton(self.mainLayoutWidget)
        #self.closeCamera.setGeometry(QtCore.QRect(210, 100, 75, 23))
        self.closeCamera.setObjectName("")
        self.closeCamera.setIcon(QtGui.QIcon('len.png'))
        self.closeCamera.setIconSize(QtCore.QSize(20,20))
        self.closeCamera.setStyleSheet("border:1px ")
        self.closeCamera.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)   
        self.closeCamera.setToolTip("Close Camera")

     
        self.singleShot = QtWidgets.QToolButton(self.mainLayoutWidget)
        #self.singleShot.setGeometry(QtCore.QRect(260, 100, 75, 23))
        self.singleShot.setObjectName("")
        self.singleShot.setIcon(QtGui.QIcon('next.png'))
        self.singleShot.setIconSize(QtCore.QSize(20,20))
        self.singleShot.setStyleSheet("border:1px ")
        self.singleShot.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.singleShot.setToolTip("Single Shot")


        self.continuouslyShot = QtWidgets.QToolButton(self.mainLayoutWidget)
        #self.continuouslyShot.setGeometry(QtCore.QRect(310, 100, 75, 23))
        self.continuouslyShot.setObjectName("")
        self.continuouslyShot.setIcon(QtGui.QIcon('fast-forward.png'))
        self.continuouslyShot.setIconSize(QtCore.QSize(20,20))
        self.continuouslyShot.setStyleSheet("border:1px ")
        self.continuouslyShot.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)        
        self.continuouslyShot.setToolTip("Continuously Shot")

        #buttons adding 
        self.mainLayoutButtons.addWidget(self.openCamera)
        self.mainLayoutButtons.addWidget(self.closeCamera)
        self.mainLayoutButtons.addWidget(self.singleShot)
        self.mainLayoutButtons.addWidget(self.continuouslyShot)
        self.mainLayoutButtons.addWidget(self.play)
        self.mainLayoutButtons.addWidget(self.pushButton_2)
        self.mainLayoutButtons.addWidget(self.pushButton_3)
      
        #self.gridLayout.addLayout(self.mainLayoutButtons)
        guiTemplate.setCentralWidget(self.centralwidget)    

    def ımagesTab(self):
        self.gridLayoutWidgetIm = QtWidgets.QWidget(self.Images)
        self.gridLayoutWidgetIm.setGeometry(QtCore.QRect(10, 10, 551, 121))
        self.gridLayoutWidgetIm.setObjectName("gridLayoutWidget")
        self.gridLayoutIm = QtWidgets.QGridLayout(self.gridLayoutWidgetIm)
        self.gridLayoutIm.setAlignment(QtCore.Qt.AlignLeft)
        self.gridLayoutIm.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutIm.setObjectName("gridLayout")
        

        self.checkColor = QtWidgets.QToolButton(self.gridLayoutWidgetIm)
        self.checkColor.setIcon(QtGui.QIcon('rgb.png'))
        self.checkColor.setIconSize(QtCore.QSize(20,20))
        self.checkColor.setText("Check color")
        self.checkColor.setStyleSheet("border:5px")
        self.gridLayoutIm.addWidget(self.checkColor, 0, 0, 1, 1)
        self.checkColor.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)

        self.checkGrayscale = QtWidgets.QToolButton(self.gridLayoutWidgetIm)
        self.checkGrayscale.setIcon(QtGui.QIcon('greyscale.png'))
        self.checkGrayscale.setIconSize(QtCore.QSize(20,20))
        self.checkGrayscale.setText("Check Grayscale")
        self.checkGrayscale.setStyleSheet("border:5px")
        self.gridLayoutIm.addWidget(self.checkGrayscale, 0, 1, 1, 1)        
        self.checkGrayscale.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        
        self.imageinfo = QtWidgets.QToolButton(self.gridLayoutWidgetIm)
        self.imageinfo.setIcon(QtGui.QIcon('image-information-button.png'))
        self.imageinfo.setIconSize(QtCore.QSize(20,20))
        self.imageinfo.setText("image information")
        self.imageinfo.setStyleSheet("border:5px")
        self.gridLayoutIm.addWidget(self.imageinfo, 0, 2, 1, 1)         
        self.imageinfo.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)

        self.calculateVol = QtWidgets.QToolButton(self.gridLayoutWidgetIm)
        self.calculateVol.setIcon(QtGui.QIcon('accounting.png'))
        self.calculateVol.setIconSize(QtCore.QSize(20,20))
        self.calculateVol.setText("calculate volume")
        self.calculateVol.setStyleSheet("border:5px")
        self.gridLayoutIm.addWidget(self.calculateVol, 0, 3, 1, 1)              
        self.calculateVol.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
       
        self.surfaceInf = QtWidgets.QToolButton(self.gridLayoutWidgetIm)
        self.surfaceInf.setIcon(QtGui.QIcon('inspection.png'))
        self.surfaceInf.setIconSize(QtCore.QSize(20,20))
        self.surfaceInf.setText("surface information")
        self.surfaceInf.setStyleSheet("border:5px")
        self.gridLayoutIm.addWidget(self.surfaceInf, 1, 0, 1, 1)      
        self.surfaceInf.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)

        self.captureImg = QtWidgets.QToolButton(self.gridLayoutWidgetIm)
        self.captureImg.setIcon(QtGui.QIcon('camera.png'))
        self.captureImg.setIconSize(QtCore.QSize(20,20))
        self.captureImg.setText("surface information")
        self.captureImg.setStyleSheet("border:5px")
        self.gridLayoutIm.addWidget(self.captureImg, 1, 1, 1, 1)                   
        self.captureImg.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        
        self.loadAndSaveImg = QtWidgets.QToolButton(self.gridLayoutWidgetIm)
        self.loadAndSaveImg.setIcon(QtGui.QIcon('data-transfer.png'))
        self.loadAndSaveImg.setIconSize(QtCore.QSize(20,20))
        self.loadAndSaveImg.setText("load and save img")
        self.loadAndSaveImg.setStyleSheet("border:5px")
        self.gridLayoutIm.addWidget(self.loadAndSaveImg, 1, 2, 1, 1)        
        self.loadAndSaveImg.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)

        self.cutImg = QtWidgets.QToolButton(self.gridLayoutWidgetIm)
        self.cutImg.setIcon(QtGui.QIcon('cut-with-scissors.png'))
        self.cutImg.setIconSize(QtCore.QSize(20,20))
        self.cutImg.setText("cut image")
        self.cutImg.setStyleSheet("border:5px")
        self.gridLayoutIm.addWidget(self.cutImg, 1, 3, 1, 1)   
        self.cutImg.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)

        self.copyImg = QtWidgets.QToolButton(self.gridLayoutWidgetIm)
        self.copyImg.setIcon(QtGui.QIcon('document.png'))
        self.copyImg.setIconSize(QtCore.QSize(20,20))
        self.copyImg.setText("copy image")
        self.copyImg.setStyleSheet("border:5px")
        self.gridLayoutIm.addWidget(self.copyImg, 0, 4, 1, 1)    
        self.copyImg.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)

        self.pasteImg = QtWidgets.QToolButton(self.gridLayoutWidgetIm)
        self.pasteImg.setIcon(QtGui.QIcon('paste-on-document.png'))
        self.pasteImg.setIconSize(QtCore.QSize(20,20))
        self.pasteImg.setText("paste image")
        self.pasteImg.setStyleSheet("border:5px")
        self.gridLayoutIm.addWidget(self.pasteImg, 1, 4, 1, 1)   
        self.pasteImg.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)

        # self.toolButton_8 = QtWidgets.QToolButton(self.gridLayoutWidget)
        # self.toolButton_8.setObjectName("toolButton_8")
        # self.gridLayout.addWidget(self.toolButton_8, 1, 0, 1, 1)
  
        self.Images.setLayout(self.gridLayoutIm)

    def transformTab(self):  
        self.gridLayoutWidget = QtWidgets.QWidget(self.Images)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 551, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setAlignment(QtCore.Qt.AlignLeft)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")


        self.flipp = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.flipp.setIcon(QtGui.QIcon('reflect.png'))
        self.flipp.setIconSize(QtCore.QSize(20,20))
        self.flipp.setText("Flip")
        self.flipp.setStyleSheet("border:5px")
        self.gridLayout.addWidget(self.flipp, 0, 0, 1, 1)
        self.flipp.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)  

        self.rotation = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.rotation.setIcon(QtGui.QIcon('vr.png'))
        self.rotation.setIconSize(QtCore.QSize(20,20))
        self.rotation.setText("Rotation")
        self.rotation.setStyleSheet("border:5px")
        self.gridLayout.addWidget(self.rotation, 0, 1, 1, 1)
        self.rotation.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)

        self.affineTrns = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.affineTrns.setIcon(QtGui.QIcon('resize.png'))
        self.affineTrns.setIconSize(QtCore.QSize(20,20))
        self.affineTrns.setText("Affine Transform")
        self.affineTrns.setStyleSheet("border:5px")
        self.gridLayout.addWidget(self.affineTrns, 0, 2, 1, 1)
        self.affineTrns.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)        
       
        self.rotateCanvas = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.rotateCanvas.setIcon(QtGui.QIcon('painting.png'))
        self.rotateCanvas.setIconSize(QtCore.QSize(20,20))
        self.rotateCanvas.setText("Rotate canvas ")
        self.rotateCanvas.setStyleSheet("border:5px")
        self.gridLayout.addWidget(self.rotateCanvas, 1, 0, 1, 1)
        self.rotateCanvas.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)        

        self.adjustSurface = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.adjustSurface.setIcon(QtGui.QIcon('resize.png'))
        self.adjustSurface.setIconSize(QtCore.QSize(20,20))
        self.adjustSurface.setText("Adjust Surface")
        self.adjustSurface.setStyleSheet("border:5px")
        self.gridLayout.addWidget(self.adjustSurface, 1, 1, 1, 1)
        self.adjustSurface.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)        

        self.limitSurface = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.limitSurface.setIcon(QtGui.QIcon('fence.png'))
        self.limitSurface.setIconSize(QtCore.QSize(20,20))
        self.limitSurface.setText("Limit Surface")
        self.limitSurface.setStyleSheet("border:5px")
        self.gridLayout.addWidget(self.limitSurface, 1, 2, 1, 1)
        self.limitSurface.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)        

        self.Transform.setLayout(self.gridLayout)

    def retranslateUi(self, guiTemplate):
        _translate = QtCore.QCoreApplication.translate
        guiTemplate.setWindowTitle(_translate("guiTemplate", "Defect Detection Control Unit"))
        guiTemplate.setWindowIcon(QtGui.QIcon('camera-shutter.png'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Common), _translate("guiTemplate", "Common"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Data), _translate("guiTemplate", "Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Devices), _translate("guiTemplate", "Devices"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Filter), _translate("guiTemplate", "Filter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Images), _translate("guiTemplate", "Images"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Transform), _translate("guiTemplate", "Transform"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ProgramExecution), _translate("guiTemplate", "ProgramExecution"))
        self.Tools.setToolTip(_translate("guiTemplate", "<html><head/><body><p>image navi</p></body></html>"))
        self.Tools.setItemText(self.Tools.indexOf(self.imageNavGroupBox), _translate("guiTemplate", "Image Navigator"))
        self.Tools.setItemText(self.Tools.indexOf(self.pixInfoGroup), _translate("guiTemplate", "Pixel Information"))
        # self.play.setText(_translate("guiTemplate", "play"))
        # self.pushButton_2.setText(_translate("guiTemplate", "pause"))
        # self.pushButton_3.setText(_translate("guiTemplate", "stop"))
       

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    guiTemplate = QtWidgets.QMainWindow()
    ui = Ui_guiTemplate()
    ui.setupUi(guiTemplate)
    guiTemplate.show()
    sys.exit(app.exec_())  