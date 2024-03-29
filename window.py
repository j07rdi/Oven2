# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(958, 676)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 75, 961, 311))
        self.graphicsView.setObjectName("graphicsView")
        self.Button_holdRes = QtWidgets.QPushButton(self.centralwidget)
        self.Button_holdRes.setGeometry(QtCore.QRect(770, 10, 161, 51))
        self.Button_holdRes.setCheckable(True)
        self.Button_holdRes.setObjectName("Button_holdRes")
        self.comboBox_stepper_ports = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_stepper_ports.setGeometry(QtCore.QRect(20, 0, 211, 32))
        self.comboBox_stepper_ports.setCurrentText("")
        self.comboBox_stepper_ports.setObjectName("comboBox_stepper_ports")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 385, 961, 260))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_status = QtWidgets.QLabel(self.tab)
        self.label_status.setGeometry(QtCore.QRect(20, 160, 59, 16))
        self.label_status.setObjectName("label_status")
        self.label_position = QtWidgets.QLabel(self.tab)
        self.label_position.setGeometry(QtCore.QRect(80, 160, 71, 16))
        self.label_position.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_position.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_position.setObjectName("label_position")
        self.label_speed = QtWidgets.QLabel(self.tab)
        self.label_speed.setGeometry(QtCore.QRect(160, 160, 59, 16))
        self.label_speed.setObjectName("label_speed")
        self.dial_FS = QtWidgets.QDial(self.tab)
        self.dial_FS.setGeometry(QtCore.QRect(850, 60, 101, 111))
        self.dial_FS.setMinimum(50)
        self.dial_FS.setMaximum(1850)
        self.dial_FS.setSingleStep(10)
        self.dial_FS.setPageStep(10)
        self.dial_FS.setSliderPosition(200)
        self.dial_FS.setTracking(True)
        self.dial_FS.setWrapping(False)
        self.dial_FS.setNotchTarget(2.0)
        self.dial_FS.setNotchesVisible(True)
        self.dial_FS.setObjectName("dial_FS")
        self.hSlider = QtWidgets.QSlider(self.tab)
        self.hSlider.setEnabled(True)
        self.hSlider.setGeometry(QtCore.QRect(160, 100, 621, 31))
        self.hSlider.setMaximum(100)
        self.hSlider.setPageStep(100)
        self.hSlider.setOrientation(QtCore.Qt.Horizontal)
        self.hSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.hSlider.setTickInterval(0)
        self.hSlider.setObjectName("hSlider")
        self.pushButton_start = QtWidgets.QPushButton(self.tab)
        self.pushButton_start.setGeometry(QtCore.QRect(150, 0, 181, 51))
        self.pushButton_start.setObjectName("pushButton_start")
        self.Button_Out = QtWidgets.QPushButton(self.tab)
        self.Button_Out.setGeometry(QtCore.QRect(330, 0, 181, 51))
        self.Button_Out.setCheckable(False)
        self.Button_Out.setAutoRepeat(True)
        self.Button_Out.setAutoRepeatDelay(1)
        self.Button_Out.setAutoRepeatInterval(1)
        self.Button_Out.setObjectName("Button_Out")
        self.Button_In = QtWidgets.QPushButton(self.tab)
        self.Button_In.setGeometry(QtCore.QRect(510, 0, 181, 51))
        self.Button_In.setCheckable(False)
        self.Button_In.setAutoRepeat(True)
        self.Button_In.setAutoRepeatDelay(1)
        self.Button_In.setAutoRepeatInterval(1)
        self.Button_In.setObjectName("Button_In")
        self.label_test = QtWidgets.QLabel(self.tab)
        self.label_test.setGeometry(QtCore.QRect(20, 190, 461, 16))
        self.label_test.setObjectName("label_test")
        self.lineEdit_FS = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_FS.setGeometry(QtCore.QRect(852, 40, 91, 21))
        self.lineEdit_FS.setObjectName("lineEdit_FS")
        self.text_FS = QtWidgets.QLabel(self.tab)
        self.text_FS.setGeometry(QtCore.QRect(160, 140, 59, 16))
        self.text_FS.setObjectName("text_FS")
        self.text_Pos = QtWidgets.QLabel(self.tab)
        self.text_Pos.setGeometry(QtCore.QRect(80, 140, 71, 16))
        self.text_Pos.setObjectName("text_Pos")
        self.text_pos = QtWidgets.QLabel(self.tab)
        self.text_pos.setGeometry(QtCore.QRect(20, 140, 59, 16))
        self.text_pos.setObjectName("text_pos")
        self.pushButton_go = QtWidgets.QCommandLinkButton(self.tab)
        self.pushButton_go.setGeometry(QtCore.QRect(530, 61, 81, 31))
        self.pushButton_go.setObjectName("pushButton_go")
        self.spinBox_position = QtWidgets.QSpinBox(self.tab)
        self.spinBox_position.setGeometry(QtCore.QRect(430, 68, 101, 20))
        self.spinBox_position.setAccelerated(True)
        self.spinBox_position.setKeyboardTracking(False)
        self.spinBox_position.setSingleStep(1)
        self.spinBox_position.setObjectName("spinBox_position")
        self.spinBox_simTemp = QtWidgets.QSpinBox(self.tab)
        self.spinBox_simTemp.setGeometry(QtCore.QRect(490, 170, 111, 22))
        self.spinBox_simTemp.setMaximum(235)
        self.spinBox_simTemp.setProperty("value", 20)
        self.spinBox_simTemp.setObjectName("spinBox_simTemp")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.spinBox_maxTravel = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_maxTravel.setGeometry(QtCore.QRect(10, 183, 91, 20))
        self.spinBox_maxTravel.setMaximum(3000)
        self.spinBox_maxTravel.setProperty("value", 830)
        self.spinBox_maxTravel.setObjectName("spinBox_maxTravel")
        self.Button_getParams = QtWidgets.QPushButton(self.tab_2)
        self.Button_getParams.setGeometry(QtCore.QRect(820, 10, 113, 32))
        self.Button_getParams.setObjectName("Button_getParams")
        self.textEdit_Params = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_Params.setGeometry(QtCore.QRect(670, 0, 151, 201))
        self.textEdit_Params.setObjectName("textEdit_Params")
        self.lineEdit_Param_to_chg = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_Param_to_chg.setGeometry(QtCore.QRect(830, 60, 111, 20))
        self.lineEdit_Param_to_chg.setObjectName("lineEdit_Param_to_chg")
        self.text_params = QtWidgets.QLabel(self.tab_2)
        self.text_params.setGeometry(QtCore.QRect(830, 40, 59, 16))
        self.text_params.setObjectName("text_params")
        self.lineEdit_cmdValue = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_cmdValue.setGeometry(QtCore.QRect(830, 110, 113, 21))
        self.lineEdit_cmdValue.setMouseTracking(False)
        self.lineEdit_cmdValue.setObjectName("lineEdit_cmdValue")
        self.text_value = QtWidgets.QLabel(self.tab_2)
        self.text_value.setGeometry(QtCore.QRect(830, 90, 91, 16))
        self.text_value.setObjectName("text_value")
        self.Button_ParamSend = QtWidgets.QPushButton(self.tab_2)
        self.Button_ParamSend.setGeometry(QtCore.QRect(822, 141, 113, 41))
        self.Button_ParamSend.setObjectName("Button_ParamSend")
        self.text_Min_FS = QtWidgets.QLabel(self.tab_2)
        self.text_Min_FS.setGeometry(QtCore.QRect(110, 24, 59, 16))
        self.text_Min_FS.setObjectName("text_Min_FS")
        self.text_max_FS = QtWidgets.QLabel(self.tab_2)
        self.text_max_FS.setGeometry(QtCore.QRect(110, 4, 59, 16))
        self.text_max_FS.setObjectName("text_max_FS")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(390, 30, 231, 161))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.spinBox_home = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_home.setGeometry(QtCore.QRect(10, 68, 91, 22))
        self.spinBox_home.setObjectName("spinBox_home")
        self.spinBox_dripping = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_dripping.setGeometry(QtCore.QRect(10, 137, 91, 22))
        self.spinBox_dripping.setMaximum(830)
        self.spinBox_dripping.setProperty("value", 670)
        self.spinBox_dripping.setObjectName("spinBox_dripping")
        self.spinBox_coolDown = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_coolDown.setGeometry(QtCore.QRect(10, 91, 91, 22))
        self.spinBox_coolDown.setMaximum(830)
        self.spinBox_coolDown.setProperty("value", 20)
        self.spinBox_coolDown.setObjectName("spinBox_coolDown")
        self.spinBox_preheat = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_preheat.setGeometry(QtCore.QRect(10, 114, 91, 22))
        self.spinBox_preheat.setMaximum(830)
        self.spinBox_preheat.setProperty("value", 320)
        self.spinBox_preheat.setObjectName("spinBox_preheat")
        self.text_locations = QtWidgets.QLabel(self.tab_2)
        self.text_locations.setGeometry(QtCore.QRect(10, 50, 101, 16))
        self.text_locations.setObjectName("text_locations")
        self.spinBox_maxFS = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_maxFS.setGeometry(QtCore.QRect(10, 0, 91, 22))
        self.spinBox_maxFS.setKeyboardTracking(False)
        self.spinBox_maxFS.setMaximum(10000)
        self.spinBox_maxFS.setProperty("value", 500)
        self.spinBox_maxFS.setObjectName("spinBox_maxFS")
        self.spinBox_minFS = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_minFS.setGeometry(QtCore.QRect(10, 22, 91, 22))
        self.spinBox_minFS.setMinimum(1)
        self.spinBox_minFS.setMaximum(1000)
        self.spinBox_minFS.setProperty("value", 50)
        self.spinBox_minFS.setObjectName("spinBox_minFS")
        self.spinBox_critical = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_critical.setGeometry(QtCore.QRect(10, 160, 91, 22))
        self.spinBox_critical.setMaximum(830)
        self.spinBox_critical.setProperty("value", 740)
        self.spinBox_critical.setObjectName("spinBox_critical")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(100, 70, 51, 131))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_home = QtWidgets.QLabel(self.widget)
        self.text_home.setObjectName("text_home")
        self.verticalLayout.addWidget(self.text_home)
        self.text_cool = QtWidgets.QLabel(self.widget)
        self.text_cool.setObjectName("text_cool")
        self.verticalLayout.addWidget(self.text_cool)
        self.text_preheat = QtWidgets.QLabel(self.widget)
        self.text_preheat.setObjectName("text_preheat")
        self.verticalLayout.addWidget(self.text_preheat)
        self.text_drip = QtWidgets.QLabel(self.widget)
        self.text_drip.setObjectName("text_drip")
        self.verticalLayout.addWidget(self.text_drip)
        self.text_critical = QtWidgets.QLabel(self.widget)
        self.text_critical.setObjectName("text_critical")
        self.verticalLayout.addWidget(self.text_critical)
        self.text_reflow = QtWidgets.QLabel(self.widget)
        self.text_reflow.setObjectName("text_reflow")
        self.verticalLayout.addWidget(self.text_reflow)
        self.tabWidget.addTab(self.tab_2, "")
        self.comboBox_temp_ports = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_temp_ports.setGeometry(QtCore.QRect(240, 0, 211, 32))
        self.comboBox_temp_ports.setObjectName("comboBox_temp_ports")
        self.lineEdit_gCommand = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_gCommand.setGeometry(QtCore.QRect(480, 4, 151, 21))
        self.lineEdit_gCommand.setMouseTracking(False)
        self.lineEdit_gCommand.setToolTip("")
        self.lineEdit_gCommand.setToolTipDuration(4)
        self.lineEdit_gCommand.setStatusTip("")
        self.lineEdit_gCommand.setWhatsThis("")
        self.lineEdit_gCommand.setInputMask("")
        self.lineEdit_gCommand.setPlaceholderText("")
        self.lineEdit_gCommand.setObjectName("lineEdit_gCommand")
        self.Button_cmd = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Button_cmd.setGeometry(QtCore.QRect(632, -2, 71, 31))
        self.Button_cmd.setObjectName("Button_cmd")
        self.label_temp0 = QtWidgets.QLabel(self.centralwidget)
        self.label_temp0.setGeometry(QtCore.QRect(10, 50, 51, 21))
        self.label_temp0.setObjectName("label_temp0")
        self.text_temp0 = QtWidgets.QLabel(self.centralwidget)
        self.text_temp0.setGeometry(QtCore.QRect(10, 30, 59, 16))
        self.text_temp0.setObjectName("text_temp0")
        self.label_temp0_delta = QtWidgets.QLabel(self.centralwidget)
        self.label_temp0_delta.setGeometry(QtCore.QRect(90, 50, 51, 21))
        self.label_temp0_delta.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temp0_delta.setObjectName("label_temp0_delta")
        self.Button_home = QtWidgets.QPushButton(self.centralwidget)
        self.Button_home.setGeometry(QtCore.QRect(500, 30, 113, 32))
        self.Button_home.setObjectName("Button_home")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 958, 22))
        self.menubar.setObjectName("menubar")
        self.menumRo_Vapor_Phase = QtWidgets.QMenu(self.menubar)
        self.menumRo_Vapor_Phase.setObjectName("menumRo_Vapor_Phase")
        self.menutest = QtWidgets.QMenu(self.menubar)
        self.menutest.setObjectName("menutest")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menumRo_Vapor_Phase.menuAction())
        self.menubar.addAction(self.menutest.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_holdRes.setText(_translate("MainWindow", "HOLD"))
        self.label_status.setText(_translate("MainWindow", "?"))
        self.label_position.setText(_translate("MainWindow", "?"))
        self.label_speed.setText(_translate("MainWindow", "?"))
        self.pushButton_start.setText(_translate("MainWindow", "START!"))
        self.Button_Out.setText(_translate("MainWindow", "Out"))
        self.Button_In.setText(_translate("MainWindow", "In"))
        self.label_test.setText(_translate("MainWindow", "Test"))
        self.text_FS.setText(_translate("MainWindow", "FS:"))
        self.text_Pos.setText(_translate("MainWindow", "Pos (mm):"))
        self.text_pos.setText(_translate("MainWindow", "Status:"))
        self.pushButton_go.setText(_translate("MainWindow", "Go!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.Button_getParams.setText(_translate("MainWindow", "Get Params"))
        self.lineEdit_Param_to_chg.setText(_translate("MainWindow", "0"))
        self.text_params.setText(_translate("MainWindow", "Param #:"))
        self.text_value.setText(_translate("MainWindow", "Value (new):"))
        self.Button_ParamSend.setText(_translate("MainWindow", "Send"))
        self.text_Min_FS.setText(_translate("MainWindow", "Min FS"))
        self.text_max_FS.setText(_translate("MainWindow", "Max FS"))
        self.text_locations.setText(_translate("MainWindow", "Locations (mm):"))
        self.text_home.setText(_translate("MainWindow", "Home"))
        self.text_cool.setText(_translate("MainWindow", "Cool"))
        self.text_preheat.setText(_translate("MainWindow", "PreHeat"))
        self.text_drip.setText(_translate("MainWindow", "Drip"))
        self.text_critical.setText(_translate("MainWindow", "Critical"))
        self.text_reflow.setText(_translate("MainWindow", "Reflow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.lineEdit_gCommand.setText(_translate("MainWindow", "$"))
        self.Button_cmd.setText(_translate("MainWindow", "Send"))
        self.label_temp0.setText(_translate("MainWindow", "?"))
        self.text_temp0.setText(_translate("MainWindow", "Temp0:"))
        self.label_temp0_delta.setText(_translate("MainWindow", "?"))
        self.Button_home.setText(_translate("MainWindow", "Home"))
        self.menumRo_Vapor_Phase.setTitle(_translate("MainWindow", "mRo Vapor Phase"))
        self.menutest.setTitle(_translate("MainWindow", "test"))


from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
