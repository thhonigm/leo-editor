# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'qt_main.ui'
#
# Created: Fri Apr 24 13:52:17 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import QtCore, QtGui
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(691, 635)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks | QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtGui.QSplitter(self.splitter_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.leo_outline_frame = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leo_outline_frame.sizePolicy().hasHeightForWidth())
        self.leo_outline_frame.setSizePolicy(sizePolicy)
        self.leo_outline_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.leo_outline_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.leo_outline_frame.setLineWidth(1)
        self.leo_outline_frame.setObjectName("leo_outline_frame")
        self.leo_outline_grid = QtGui.QGridLayout(self.leo_outline_frame)
        self.leo_outline_grid.setMargin(0)
        self.leo_outline_grid.setObjectName("leo_outline_grid")
        self.leo_outline_inner_frame = QtGui.QFrame(self.leo_outline_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leo_outline_inner_frame.sizePolicy().hasHeightForWidth())
        self.leo_outline_inner_frame.setSizePolicy(sizePolicy)
        self.leo_outline_inner_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.leo_outline_inner_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.leo_outline_inner_frame.setObjectName("leo_outline_inner_frame")
        self.gridLayout_3 = QtGui.QGridLayout(self.leo_outline_inner_frame)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.treeWidget = QtGui.QTreeWidget(self.leo_outline_inner_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.treeWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout_3.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.leo_outline_grid.addWidget(self.leo_outline_inner_frame, 0, 0, 1, 1)
        self.leo_log_frame = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leo_log_frame.sizePolicy().hasHeightForWidth())
        self.leo_log_frame.setSizePolicy(sizePolicy)
        self.leo_log_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.leo_log_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.leo_log_frame.setLineWidth(1)
        self.leo_log_frame.setObjectName("leo_log_frame")
        self.leo_log_grid = QtGui.QGridLayout(self.leo_log_frame)
        self.leo_log_grid.setMargin(0)
        self.leo_log_grid.setObjectName("leo_log_grid")
        self.leo_log_inner_frame = QtGui.QFrame(self.leo_log_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leo_log_inner_frame.sizePolicy().hasHeightForWidth())
        self.leo_log_inner_frame.setSizePolicy(sizePolicy)
        self.leo_log_inner_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.leo_log_inner_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.leo_log_inner_frame.setObjectName("leo_log_inner_frame")
        self.gridLayout_7 = QtGui.QGridLayout(self.leo_log_inner_frame)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget = QtGui.QTabWidget(self.leo_log_inner_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab) # Was QtGui.QTextBrowser.
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.findPattern = QtGui.QLineEdit(self.tab_2)
        self.findPattern.setObjectName("findPattern")
        self.gridLayout_5.addWidget(self.findPattern, 0, 1, 1, 1)
        self.findChange = QtGui.QLineEdit(self.tab_2)
        self.findChange.setObjectName("findChange")
        self.gridLayout_5.addWidget(self.findChange, 1, 1, 1, 1)
        self.checkBoxWholeWord = QtGui.QCheckBox(self.tab_2)
        self.checkBoxWholeWord.setObjectName("checkBoxWholeWord")
        self.gridLayout_5.addWidget(self.checkBoxWholeWord, 2, 0, 1, 1)
        self.checkBoxEntireOutline = QtGui.QCheckBox(self.tab_2)
        self.checkBoxEntireOutline.setObjectName("checkBoxEntireOutline")
        self.gridLayout_5.addWidget(self.checkBoxEntireOutline, 2, 1, 1, 1)
        self.checkBoxIgnoreCase = QtGui.QCheckBox(self.tab_2)
        self.checkBoxIgnoreCase.setObjectName("checkBoxIgnoreCase")
        self.gridLayout_5.addWidget(self.checkBoxIgnoreCase, 3, 0, 1, 1)
        self.checkBoxSuboutlineOnly = QtGui.QCheckBox(self.tab_2)
        self.checkBoxSuboutlineOnly.setObjectName("checkBoxSuboutlineOnly")
        self.gridLayout_5.addWidget(self.checkBoxSuboutlineOnly, 3, 1, 1, 1)
        self.checkBoxWrapAround = QtGui.QCheckBox(self.tab_2)
        self.checkBoxWrapAround.setObjectName("checkBoxWrapAround")
        self.gridLayout_5.addWidget(self.checkBoxWrapAround, 4, 0, 1, 1)
        self.checkBoxNodeOnly = QtGui.QCheckBox(self.tab_2)
        self.checkBoxNodeOnly.setObjectName("checkBoxNodeOnly")
        self.gridLayout_5.addWidget(self.checkBoxNodeOnly, 4, 1, 1, 1)
        self.checkBoxReverse = QtGui.QCheckBox(self.tab_2)
        self.checkBoxReverse.setObjectName("checkBoxReverse")
        self.gridLayout_5.addWidget(self.checkBoxReverse, 5, 0, 1, 1)
        self.checkBoxSearchHeadline = QtGui.QCheckBox(self.tab_2)
        self.checkBoxSearchHeadline.setObjectName("checkBoxSearchHeadline")
        self.gridLayout_5.addWidget(self.checkBoxSearchHeadline, 5, 1, 1, 1)
        self.checkBoxRexexp = QtGui.QCheckBox(self.tab_2)
        self.checkBoxRexexp.setObjectName("checkBoxRexexp")
        self.gridLayout_5.addWidget(self.checkBoxRexexp, 6, 0, 1, 1)
        self.checkBoxSearchBody = QtGui.QCheckBox(self.tab_2)
        self.checkBoxSearchBody.setObjectName("checkBoxSearchBody")
        self.gridLayout_5.addWidget(self.checkBoxSearchBody, 6, 1, 1, 1)
        self.checkBoxMarkFinds = QtGui.QCheckBox(self.tab_2)
        self.checkBoxMarkFinds.setObjectName("checkBoxMarkFinds")
        self.gridLayout_5.addWidget(self.checkBoxMarkFinds, 7, 0, 1, 1)
        self.checkBoxMarkChanges = QtGui.QCheckBox(self.tab_2)
        self.checkBoxMarkChanges.setObjectName("checkBoxMarkChanges")
        self.gridLayout_5.addWidget(self.checkBoxMarkChanges, 7, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.leo_spell_tab = QtGui.QWidget()
        self.leo_spell_tab.setObjectName("leo_spell_tab")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.leo_spell_tab)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setMargin(2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.leo_spell_panel = QtGui.QFrame(self.leo_spell_tab)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.leo_spell_panel.setPalette(palette)
        self.leo_spell_panel.setAutoFillBackground(False)
        self.leo_spell_panel.setFrameShape(QtGui.QFrame.NoFrame)
        self.leo_spell_panel.setFrameShadow(QtGui.QFrame.Plain)
        self.leo_spell_panel.setLineWidth(0)
        self.leo_spell_panel.setObjectName("leo_spell_panel")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.leo_spell_panel)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setSpacing(2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.leo_spell_btn_Add = QtGui.QPushButton(self.leo_spell_panel)
        self.leo_spell_btn_Add.setObjectName("leo_spell_btn_Add")
        self.gridLayout_6.addWidget(self.leo_spell_btn_Add, 2, 1, 1, 1)
        self.leo_spell_btn_Find = QtGui.QPushButton(self.leo_spell_panel)
        self.leo_spell_btn_Find.setObjectName("leo_spell_btn_Find")
        self.gridLayout_6.addWidget(self.leo_spell_btn_Find, 2, 0, 1, 1)
        self.leo_spell_btn_Change = QtGui.QPushButton(self.leo_spell_panel)
        self.leo_spell_btn_Change.setObjectName("leo_spell_btn_Change")
        self.gridLayout_6.addWidget(self.leo_spell_btn_Change, 3, 0, 1, 1)
        self.leo_spell_btn_FindChange = QtGui.QPushButton(self.leo_spell_panel)
        self.leo_spell_btn_FindChange.setObjectName("leo_spell_btn_FindChange")
        self.gridLayout_6.addWidget(self.leo_spell_btn_FindChange, 3, 1, 1, 1)
        self.leo_spell_btn_Ignore = QtGui.QPushButton(self.leo_spell_panel)
        self.leo_spell_btn_Ignore.setObjectName("leo_spell_btn_Ignore")
        self.gridLayout_6.addWidget(self.leo_spell_btn_Ignore, 4, 0, 1, 1)
        self.leo_spell_btn_Hide = QtGui.QPushButton(self.leo_spell_panel)
        self.leo_spell_btn_Hide.setCheckable(False)
        self.leo_spell_btn_Hide.setObjectName("leo_spell_btn_Hide")
        self.gridLayout_6.addWidget(self.leo_spell_btn_Hide, 4, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem, 5, 0, 1, 1)
        self.leo_spell_listBox = QtGui.QListWidget(self.leo_spell_panel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leo_spell_listBox.sizePolicy().hasHeightForWidth())
        self.leo_spell_listBox.setSizePolicy(sizePolicy)
        self.leo_spell_listBox.setMinimumSize(QtCore.QSize(0, 0))
        self.leo_spell_listBox.setMaximumSize(QtCore.QSize(150, 150))
        self.leo_spell_listBox.setObjectName("leo_spell_listBox")
        self.gridLayout_6.addWidget(self.leo_spell_listBox, 1, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 2, 2, 1, 1)
        self.leo_spell_label = QtGui.QLabel(self.leo_spell_panel)
        self.leo_spell_label.setObjectName("leo_spell_label")
        self.gridLayout_6.addWidget(self.leo_spell_label, 0, 0, 1, 2)
        self.verticalLayout_6.addLayout(self.gridLayout_6)
        self.verticalLayout_5.addWidget(self.leo_spell_panel)
        self.tabWidget.addTab(self.leo_spell_tab, "")
        self.gridLayout_7.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.leo_log_grid.addWidget(self.leo_log_inner_frame, 0, 0, 1, 1)
        self.leo_body_frame = QtGui.QFrame(self.splitter_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leo_body_frame.sizePolicy().hasHeightForWidth())
        self.leo_body_frame.setSizePolicy(sizePolicy)
        self.leo_body_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.leo_body_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.leo_body_frame.setLineWidth(1)
        self.leo_body_frame.setObjectName("leo_body_frame")
        self.leo_body_grid = QtGui.QGridLayout(self.leo_body_frame)
        self.leo_body_grid.setMargin(0)
        self.leo_body_grid.setObjectName("leo_body_grid")
        self.leo_body_inner_frame = QtGui.QFrame(self.leo_body_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leo_body_inner_frame.sizePolicy().hasHeightForWidth())
        self.leo_body_inner_frame.setSizePolicy(sizePolicy)
        self.leo_body_inner_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.leo_body_inner_frame.setFrameShadow(QtGui.QFrame.Plain)
        self.leo_body_inner_frame.setLineWidth(1)
        self.leo_body_inner_frame.setObjectName("leo_body_inner_frame")
        self.grid = QtGui.QGridLayout(self.leo_body_inner_frame)
        self.grid.setMargin(0)
        self.grid.setObjectName("grid")
        self.stackedWidget = QtGui.QStackedWidget(self.leo_body_inner_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setAcceptDrops(True)
        self.stackedWidget.setLineWidth(1)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit = Qsci.QsciScintilla(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtGui.QFrame.Plain)
        self.textEdit.setLineWidth(0)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.richTextEdit = QtWidgets.QTextEdit(self.page_2) ### Was QtGui.QTextEdit.
        self.richTextEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.richTextEdit.setFrameShadow(QtGui.QFrame.Plain)
        self.richTextEdit.setLineWidth(0)
        self.richTextEdit.setObjectName("richTextEdit")
        self.verticalLayout_4.addWidget(self.richTextEdit)
        self.stackedWidget.addWidget(self.page_2)
        self.grid.addWidget(self.stackedWidget, 0, 0, 1, 1)
        self.leo_body_grid.addWidget(self.leo_body_inner_frame, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.splitter_2)
        self.leo_minibuffer_frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leo_minibuffer_frame.sizePolicy().hasHeightForWidth())
        self.leo_minibuffer_frame.setSizePolicy(sizePolicy)
        self.leo_minibuffer_frame.setMinimumSize(QtCore.QSize(100, 0))
        self.leo_minibuffer_frame.setBaseSize(QtCore.QSize(0, 0))
        self.leo_minibuffer_frame.setMidLineWidth(0)
        self.leo_minibuffer_frame.setObjectName("leo_minibuffer_frame")
        self.leo_minibuffer_layout = QtGui.QHBoxLayout(self.leo_minibuffer_frame)
        self.leo_minibuffer_layout.setSpacing(4)
        self.leo_minibuffer_layout.setContentsMargins(3, 2, 2, 0)
        self.leo_minibuffer_layout.setObjectName("leo_minibuffer_layout")
        self.label = QtGui.QLabel(self.leo_minibuffer_frame)
        self.label.setObjectName("label")
        self.leo_minibuffer_layout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.leo_minibuffer_frame)
        self.lineEdit.setObjectName("lineEdit")
        self.leo_minibuffer_layout.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.leo_minibuffer_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 691, 19))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionIPython = QtGui.QAction(MainWindow)
        self.actionIPython.setObjectName("actionIPython")
        self.label.setBuddy(self.lineEdit)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.leo_spell_btn_Add, QtCore.SIGNAL("clicked()"), MainWindow.do_leo_spell_btn_Add)
        QtCore.QObject.connect(self.leo_spell_btn_Change, QtCore.SIGNAL("clicked()"), MainWindow.do_leo_spell_btn_Change)
        QtCore.QObject.connect(self.leo_spell_btn_Find, QtCore.SIGNAL("clicked()"), MainWindow.do_leo_spell_btn_Find)
        QtCore.QObject.connect(self.leo_spell_btn_FindChange, QtCore.SIGNAL("clicked()"), MainWindow.do_leo_spell_btn_FindChange)
        QtCore.QObject.connect(self.leo_spell_btn_Hide, QtCore.SIGNAL("clicked()"), MainWindow.do_leo_spell_btn_Hide)
        QtCore.QObject.connect(self.leo_spell_btn_Ignore, QtCore.SIGNAL("clicked()"), MainWindow.do_leo_spell_btn_Ignore)
        QtCore.QObject.connect(self.leo_spell_listBox, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem*)"), MainWindow.do_leo_spell_btn_FindChange)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Leo", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxWholeWord.setText(QtGui.QApplication.translate("MainWindow", "Whole Word", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxEntireOutline.setText(QtGui.QApplication.translate("MainWindow", "Entire Outline", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxIgnoreCase.setText(QtGui.QApplication.translate("MainWindow", "Ignore Case", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxSuboutlineOnly.setText(QtGui.QApplication.translate("MainWindow", "Suboutline Only", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxWrapAround.setText(QtGui.QApplication.translate("MainWindow", "Wrap Around", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxNodeOnly.setText(QtGui.QApplication.translate("MainWindow", "Node Only", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxReverse.setText(QtGui.QApplication.translate("MainWindow", "Reverse", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxSearchHeadline.setText(QtGui.QApplication.translate("MainWindow", "Search Headline", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxRexexp.setText(QtGui.QApplication.translate("MainWindow", "Regexp", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxSearchBody.setText(QtGui.QApplication.translate("MainWindow", "Search Body", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxMarkFinds.setText(QtGui.QApplication.translate("MainWindow", "Mark Finds", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxMarkChanges.setText(QtGui.QApplication.translate("MainWindow", "Mark Changes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Find:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Change:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Page", None, QtGui.QApplication.UnicodeUTF8))
        self.leo_spell_btn_Add.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.leo_spell_btn_Find.setText(QtGui.QApplication.translate("MainWindow", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.leo_spell_btn_Change.setText(QtGui.QApplication.translate("MainWindow", "Change", None, QtGui.QApplication.UnicodeUTF8))
        self.leo_spell_btn_FindChange.setText(QtGui.QApplication.translate("MainWindow", "Change, Find", None, QtGui.QApplication.UnicodeUTF8))
        self.leo_spell_btn_Ignore.setText(QtGui.QApplication.translate("MainWindow", "Ignore", None, QtGui.QApplication.UnicodeUTF8))
        self.leo_spell_btn_Hide.setText(QtGui.QApplication.translate("MainWindow", "Hide", None, QtGui.QApplication.UnicodeUTF8))
        self.leo_spell_label.setText(QtGui.QApplication.translate("MainWindow", "Suggestions for:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.leo_spell_tab), QtGui.QApplication.translate("MainWindow", "Spell", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Minibuffer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIPython.setText(QtGui.QApplication.translate("MainWindow", "IPython", None, QtGui.QApplication.UnicodeUTF8))
from PyQt4 import Qsci
