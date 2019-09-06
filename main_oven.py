#!/usr/bin/python3
# pyuic5 -x window.ui -o window.py
""" 
Recommended to install: 
pip install --upgrade pip
python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

#sudo apt install qtcreator pyqt5-dev-tools
#sudo apt-get install qttools5-dev-tools

#sudo adduser $USER dialout   <---- In case tty is asking for permisions all the time.. 
#sudo chmod 666 /dev/ttyACM0

"""
import subprocess
cmd = "pyuic5 -x window.ui -o window.py"
p = subprocess.Popen((cmd), shell=True, stdout=subprocess.PIPE)
p.wait()

import sys, os, platform, pty, time, threading, glob, json
import serial
import serial.tools.list_ports
import pyqtgraph as pg
from PyQt5 import QtWidgets
from PyQt5 import *
from PyQt5.QtCore import pyqtSignal, QObject, Qt, QTimer, QThread
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QShortcut, QTableWidget, QTableWidgetItem
from window import Ui_MainWindow  # importing our generated file
from temp_sim import *
from trunk import *
import pyqtgraph.exporters
from simple_pid import PID


############################################################################
############################################################################

print('Hello, mRo!', 'Python', platform.python_version(), sys.platform)

############################################################################
############################################################################
#global variables:
close_everything = 0
position = 0 #the actual position of the car. 
getParams_pressed = 0
sendCmd_pressed = 0
Button_ParamSend_pressed = 0
pushButton_go_pushed = 0
Button_Start_pressed = 0
Button_In_pressed = 0
Button_Out_pressed = 0
Button_holdRes_Pressed = 2

temp_0 = 20.0 #The actual global temp.
temp_0_rate = 0.00 #The change rate of temperature 
start = time.time() # start time of the program 
oven_state = 0 #Basically the system state of the oven
command_transfer = "" #used to send external commands, be careful 
stepper_status = ""

cycle_started = False


id = QtCore.QMetaType.type('QVector')

class mywindow(QtWidgets.QMainWindow):
    update_window_signal = pyqtSignal()


    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Threads 
        self.threadclass = ThreadClass()
        self.threadclass .start()
        self.threadclass.sig1.connect(self.graphUpdate)
        #self.connect(self.threadclass, QtCore.SIGNAL("elVal"), self.graphUpdate)
        #Signals:::
        self.ui.pushButton_start.clicked.connect(self.Button_Start_Clicked) # connecting the clicked signal with btnClicked slot
        self.ui.Button_In.clicked.connect(self.Button_In_Clicked)
        self.ui.Button_Out.clicked.connect(self.Button_Out_Clicked)
        self.ui.dial_FS.valueChanged.connect(self.dial_FS_moved)
        self.ui.lineEdit_FS.returnPressed.connect(self.lineEdit_FS_change)
        self.ui.Button_getParams.clicked.connect(self.Button_getParams_Clicked)
        self.ui.Button_cmd.clicked.connect(self.Button_cmd_Clicked)
        self.ui.lineEdit_gCommand.returnPressed.connect(self.Button_cmd_Clicked)
        self.ui.Button_ParamSend.clicked.connect(self.Button_ParamSend_Clicked)
        self.ui.spinBox_maxTravel.valueChanged.connect(self.spinBox_maxTravel_clicked)
        self.ui.spinBox_position.valueChanged.connect(self.spinBox_position_clicked)
        self.ui.hSlider.valueChanged.connect(self.hSlider_clicked)
        self.ui.pushButton_go.clicked.connect(self.pushButton_go_clicked)
        self.ui.Button_holdRes.clicked.connect(self.Button_holdRes_Clicked)
        self.ui.Button_home.clicked.connect(self.Button_home_Clicked)

        self.ui.spinBox_maxFS.valueChanged.connect(self.settingChanges)

        self.update_window_signal.connect(self.update_window_routine)
        #self.ui.tableView_Params.itemChanged.connect(self.tableSignal)
        ### Default values 
        self.ui.comboBox_temp_ports.setEnabled(False)
        self.ui.comboBox_stepper_ports.setEnabled(False)
        self.ui.Button_cmd.setEnabled(False)
        self.ui.Button_getParams.setEnabled(False)
        self.ui.Button_ParamSend.setEnabled(False)
        self.ui.dial_FS.setValue(200)
        self.ui.lineEdit_FS.setText(str(self.ui.dial_FS.value()))
        self.ui.hSlider.setMaximum(self.ui.spinBox_maxTravel.value()/10)
        self.ui.spinBox_position.setMaximum(self.ui.spinBox_maxTravel.value())

        #private variables
        self.temp_counter = 0
        self.temp_old = temp_0
        self.block_soak = 0
        self.block_peak = 0


    def graphUpdate(self, val):
        #print("Output temp is ", val)
        mins = self.temp_counter/60

        self.ui.graphicsView.plot([mins,(self.temp_counter+1)/60],[self.temp_old,val], pen='w')
        self.temp_old = val
       

        if val >= 130:
            if self.block_soak == 0:
                self.block_soak = 1
                #self.ui.graphicsView.plot([mins,mins+.5],[140,140], pen='r')
                #self.ui.graphicsView.plot([mins,mins+.5],[150,150], pen='r')
                self.ui.graphicsView.plot([mins+.5,mins+1.5],[140,140], pen='g')
                self.ui.graphicsView.plot([mins+.5,mins+1.5],[150,150], pen='g')
                self.ui.graphicsView.plot([mins+1.5,mins+2],[140,140], pen='y')
                self.ui.graphicsView.plot([mins+1.5,mins+2],[150,150], pen='y')

                self.ui.graphicsView.plot([mins,mins+.5],[130,130], pen='r')
                self.ui.graphicsView.plot([mins,mins+.5],[170,170], pen='r')
                self.ui.graphicsView.plot([mins+.5,mins+1.5],[130,130], pen='y')
                self.ui.graphicsView.plot([mins+.5,mins+1.5],[170,170], pen='y')
                self.ui.graphicsView.plot([mins+1.5,mins+2],[130,130], pen='y')
                self.ui.graphicsView.plot([mins+1.5,mins+2],[170,170], pen='y')
        if val >= 183:
            if self.block_peak == 0:
                self.block_peak = 1
                self.ui.graphicsView.plot([mins+.75,mins+.75],[183,230], pen='g')
                self.ui.graphicsView.plot([mins+1,mins+1],[183,230], pen='g')
                self.ui.graphicsView.plot([mins+.5,mins+.5],[183,230], pen='y')
                self.ui.graphicsView.plot([mins+(100/60),mins+(100/60)],[183,230], pen='y')


        self.temp_counter += 1
        self.update_window_routine()
        

    def update_window_call(self):
        self.update_window_signal.emit()

    def update_window_routine(self):
        self.repaint() 
        QApplication.processEvents()
    
    def settingChanges(self):
        ### maxFS ###
        newValue = self.ui.spinBox_maxFS.value()
        set_Setting("maxFS",newValue)
        self.ui.dial_FS.setValue(newValue)
    
    def pushButton_go_clicked(self):
        global pushButton_go_pushed
        pushButton_go_pushed = 1

    def hSlider_clicked(self):
        self.ui.spinBox_position.setValue(self.ui.hSlider.value()*10)

    def spinBox_position_clicked(self):
        self.ui.hSlider.setValue(self.ui.spinBox_position.value()/10)

    def spinBox_maxTravel_clicked(self):
        self.ui.hSlider.setMaximum(self.ui.spinBox_maxTravel.value()/10)

    def Button_ParamSend_Clicked(self):
        global Button_ParamSend_pressed
        Button_ParamSend_pressed = 1

    def Button_cmd_Clicked(self):
        global sendCmd_pressed
        sendCmd_pressed =1

    def Button_getParams_Clicked(self):
        global getParams_pressed
        getParams_pressed = 1
        self.ui.textEdit_Params.clear()
        #print("Get Params clicked")
    """def position(self, posvalue):
        count = 0
        while count < posvalue:
            count += 5
            #self.ui.progressBar.setValue(posvalue)
            time.sleep(1)"""
        
        #QApplication.processEvents()
    def dial_FS_moved(self):
        self.ui.lineEdit_FS.setText(str(self.ui.dial_FS.value()))

    def lineEdit_FS_change(self):
        self.ui.dial_FS.setValue(int(self.ui.lineEdit_FS.text()))
        self.ui.lineEdit_FS.selectAll()

    def Button_Start_Clicked(self):
        global Button_Start_pressed
        Button_Start_pressed = 1

    def Button_In_Clicked(self):
        global Button_In_pressed
        Button_In_pressed = 1 #dummy command. 
        #print("Button pressed")

    def Button_Out_Clicked(self):
        #print("Button pressed")
        global Button_Out_pressed
        Button_Out_pressed = 1

    def Button_holdRes_Clicked(self):
        global Button_holdRes_Pressed
        if self.ui.Button_holdRes.isChecked():
            Button_holdRes_Pressed = 1
            print("hold Button pressed")
        else:
            Button_holdRes_Pressed = 0
            print("hold Button released")

    def Button_home_Clicked(self):
        global command_transfer
        command_transfer = "$H\n"
        print("Homing")

    def closeEvent(self, event):
        global close_everything
        close_everything = 1
        event.accept() # let the window close

############################################################################
############################################################################
class ThreadClass(QtCore.QThread):
    sig1 = pyqtSignal(float)

    def __init__(self,parent = None):
        #super(ThreadClass, self).__init__(parent)
        QtCore.QThread.__init__(self, parent)

    def run(self):
        global temp_0

        print("helloo from QThread")
        global cycle_started
        while 1:
            if cycle_started:
                internal_val = temp_0
                self.sig1.emit(internal_val)
            QThread.msleep(1000)

            if close_everything == 1:
                return 0

############################################################################
############################################################################
#import numpy as np
#import matplotlib.pyplot as plt
#from scipy import signal
#from scipy.signal import butter, lfilter, freqz

def temp_port():
    global close_everything
    global temp_0
    global temp_0_rate
    temp_0_old = 20
    timer_temp_0_delta = time.time()
    #l = [float(1.4),float(1.4),float(1.4),float(1.4)]
    RawData = 0.01
    SmoothData = 0.01
    LPF_Beta = 0.03 # 0<ß<1


    port_received=serial_ports()
    application.ui.comboBox_temp_ports.addItems(port_received)
    application.ui.comboBox_temp_ports.setEnabled(True)

    rxset = get_Setting("Temp_COM")

    matched_success  = 0
    for x in port_received:
        if rxset == x:
            print(f'Port MATCHED!!! Selected {rxset}')
            matched_success = 1
            application.ui.comboBox_temp_ports.clear()
            application.ui.comboBox_temp_ports.addItem(rxset)
            #Setting matched port for fast loading. 
            selectedPort=rxset

    if matched_success == 0:
        print("Waiting for user to select Temperature COM Port")
        while application.ui.comboBox_temp_ports.currentText() == "Select COM":
            time.sleep(100/1000)
            if close_everything == 1: #just in case they close before choosing a port. 
                return 0
        selectedPort= application.ui.comboBox_temp_ports.currentText()
        #Saving select port for future use... 
        set_Setting("Temp_COM", selectedPort)
    
    try:
        #We need to open and close the port to properly initlize the Arduino Sketch.
        s = serial.Serial(selectedPort,115200, timeout=5)
        time.sleep(500/1000)
        s.close()
        time.sleep(500/1000)
        s = serial.Serial(selectedPort,115200, timeout=5)

    except:
        print("Unexpected error:", sys.exc_info()[0])
        s.close()
    else:
        while 1:
            time.sleep(100/1000)

            if s.inWaiting() > 0:
                read_line = s.readline()
                #print(f'temp:{read_line.decode("utf-8")}')
                if read_line.decode("utf-8")[0] == '$':
                    
                    #################################################################

                    split = read_line.decode("utf-8").split(':')
                    stripped = split[1]
                    temp_0 = float(stripped)
                    #print("test temp", temp_0)

                    stripped = stripped.strip('\r\n')

                    application.ui.label_temp0.setText(stripped + '\N{DEGREE SIGN}C')

                    #if temp_0 != temp_0_old :
                    dt = (time.time() - timer_temp_0_delta)
                    timer_temp_0_delta = time.time() #resetting timer.

                    dT = temp_0-temp_0_old
                    temp_0_old = temp_0

                    #temp_0_rate = dT / dt
                    
                    RawData = dT / dt
                    if abs(SmoothData - RawData) > .5:
                        SmoothData = SmoothData - (.5 * (SmoothData - RawData)) #low pass filter
                    else:
                        SmoothData = SmoothData - (LPF_Beta * (SmoothData - RawData)) # low pass filter

                    temp_0_rate = SmoothData

                    application.ui.label_temp0_delta.setText(f"{temp_0_rate:,.2f} \N{DEGREE SIGN}C")
                    #l.pop(0)
                    #l.append(temp_0_delta)
    
                    #print("type:", np.array(output))
                    #print(f" Delta calced: {temp_0_delta:,.2f} smooth {SmoothData:,.2f} time: {dt:,.2f}") #filtered {output:,.4f}

                    #application.update_window_call()
                    #if s.inWaiting() > 0:
                        #s.flush()
                    ##time.sleep(100/1000)


            if close_everything == 1:
                s.close()
                return 0
    


############################################################################
############################################################################

def stepper_port():

    #Global vars
    global close_everything
    global getParams_pressed
    global sendCmd_pressed
    global Button_ParamSend_pressed
    global pushButton_go_pushed
    global Button_In_pressed
    global Button_Out_pressed

    global position
    global command_transfer
    global stepper_status
    counterParams = 0
    rxstr = ""

    timer_InOut_buttons = time.time()
    timer_1 = time.time()
    #position_old = position

    value = application.ui.hSlider.value()

    port_received=serial_ports()            #reading coms available. 
    print("Ports received", port_received)
    application.ui.comboBox_stepper_ports.addItems(port_received)
    application.ui.comboBox_stepper_ports.setEnabled(True)

    rxset = get_Setting("Stepper_COM")
    
    matched_success  = 0
    for x in port_received:
        if rxset == x:
            print(f'Port MATCHED!!! {rxset}')
            matched_success = 1
            application.ui.comboBox_stepper_ports.clear()
            application.ui.comboBox_stepper_ports.addItem(rxset)
            #Setting matched port for fast loading. 
            selectedPort=rxset

    if matched_success == 0:
        while application.ui.comboBox_stepper_ports.currentText() == "Select COM":
            time.sleep(100/1000)
            if close_everything == 1:
                return 0

        selectedPort= application.ui.comboBox_stepper_ports.currentText()
        print("Ports selected ", selectedPort)
        #Saving for later use. 
        set_Setting("Stepper_COM", selectedPort)


    try:
        s = serial.Serial(selectedPort,115200, timeout=1)
        application.ui.Button_cmd.setEnabled(True)
        application.ui.Button_getParams.setEnabled(True)
        application.ui.Button_ParamSend.setEnabled(True)

    except (OSError, serial.SerialException):
        print("Error opening port ",serial.SerialException)
        s.close()
    else:
        s.write(str.encode('\r\n\r\n'))
        s.flushInput()
        time.sleep(1)
        read_line = s.readline()
        s.write(str.encode('$X\n'))
        while 1:

            if time.time() - timer_1 > 50/1000:
                timer_1 = time.time()
                s.write(str.encode('?'))

            while s.inWaiting() > 0:

                try:
                    read_line = s.readline()
                    #Status = stripped[0].strip('<')
                    #print("grbl: ",read_line.decode("utf-8"))
                    #if read_line.decode("utf-8") == "ok\r\n":
                        #print("Received OK")

                    if read_line.decode("utf-8")[0] == "<":
                                        
                        stripped = read_line.decode("utf-8").split('|')
                        stepper_status = stripped[0].strip('<')
                        application.ui.label_status.setText(stepper_status)

                        #We are extracting the middle item on the 
                        #list which includes the XYZ positions. 
                        stripped_XYZ = stripped[1].split(':')
                        stripped_XYZ = stripped_XYZ[1].split(',')
                        position = float(stripped_XYZ[0])
                        application.ui.label_position.setText(str(position))
                        
                        #application.position(position)
                        #application.ui.progressBar.setValue()
                        #print(stripped_XYZ[0])

                        stripped_FS= stripped[2].split(':')
                        stripped_FS= stripped_FS[1].split(',')
                        application.ui.label_speed.setText(stripped_FS[0])

                    elif (read_line.decode("utf-8")[0] == "$"):
                        #split_ss = read_line.split('=')
                        split_ss = read_line.decode("utf-8").split('=')

                        rxstr = rxstr + (split_ss[0]+" -> "+split_ss[1])
                        #print(rxstr)
                        #time.sleep(10/1000)
                        
                        counterParams+=1

                        if counterParams >= 34:
                            #print("All params received!")
                            try:
                                QApplication.processEvents()
                                application.ui.textEdit_Params.append(rxstr)
                                #print(rxstr)
                                QApplication.processEvents()
                                #time.sleep(400/1000)
                            except:
                                print("Unexpected error:", sys.exc_info()[0])
                    else:
                        print("grbl: ",read_line.decode("utf-8"))
                            
                except:
                    print("Unexpected error on stepper:", sys.exc_info()[0])

            #time.sleep(10/1000)
            QThread.msleep(2)
            ##########################################################
            if Button_ParamSend_pressed == 1:
                Button_ParamSend_pressed=0
                cmd_num = application.ui.lineEdit_Param_to_chg.text()
                cmd_value = application.ui.lineEdit_cmdValue.text()
                try:
                    s.write(str.encode('$'+cmd_num+'='+cmd_value+'\n'))
                except:
                    print("Unable to send cmd")

            ##########################################################

            if sendCmd_pressed == 1:
                sendCmd_pressed = 0
                cmd = application.ui.lineEdit_gCommand.text()
                print(str.encode(cmd))

                print(cmd)
                try:
                    if cmd[0] == '?':
                        s.write(str.encode(cmd))
                    elif cmd[0] == '$':
                        s.write(str.encode(cmd+'\n'))
                        
                    elif cmd[0] == 'M': 
                        s.write(str.encode(cmd+'\n'))
                        print("M dected")
                    else:
                        s.write(str.encode(cmd+'\n\r'))
                except:
                    print("Unable to send cmd")

            ##########################################################
                #This piece of code will gather the paramms
            if getParams_pressed == 1:
                try:
                    getParams_pressed = 0
                    counterParams = 0 #resetting counter
                    s.write(str.encode('$$\n'))
                    print("pressed get Params")
                    rxstr = ""
                    QThread.msleep(500)
                except:
                    print("Error")
            ##########################################################
            """
            The following piece of code will actually move the stepper manually. 
            """
            if pushButton_go_pushed == 1:
                pushButton_go_pushed = 0
                if value != application.ui.spinBox_position.value():
                    value = application.ui.spinBox_position.value()
                    s.write(str.encode('G1X'+str(value)+'F'+str(application.ui.dial_FS.value())+'\n'))
                    print(str.encode('G1X'+str(value)+'F'+str(application.ui.dial_FS.value())+'\n'))

            ##########################################################
            """
            Little function to send commands outside the function. Use with care. 
            """
            if command_transfer != None:
                if stepper_status == 'Idle':
                    s.write(str.encode(command_transfer))
                    print(f'Sending command: {command_transfer}')
                    command_transfer = None

            ##########################################################
            global Button_holdRes_Pressed
            if Button_holdRes_Pressed == 1:
                Button_holdRes_Pressed = 2
                s.write(str.encode('!\n\r'))
                application.ui.Button_holdRes.setText("Resume")


            if Button_holdRes_Pressed == 0:
                Button_holdRes_Pressed = 2
                s.write(str.encode('~\n\r'))
                application.ui.Button_holdRes.setText("Hold!")
            ##########################################################
            #application.ui.Button_In.setCheckable(True)
            #if application.ui.Button_In.isChecked() == True:
            if time.time() - timer_InOut_buttons > 50/1000:
                timer_InOut_buttons = time.time ()
                if Button_In_pressed == 1:
                    Button_In_pressed = 0
                    #print("Button is being pressed WTF?")
                    #print(str.encode('$J=X'+str(round(position)+1)+'F'+str(application.ui.dial_FS.value())+'\n'))
                    s.write(str.encode('$J=X'+str(round(position)+5)+'F'+str(application.ui.dial_FS.value())+'\n'))
                    application.ui.spinBox_position.setValue(int(position))

                if Button_Out_pressed == 1:
                    Button_Out_pressed = 0
                    #print("Button is being pressed WTF?")
                    #print(str.encode('$J=X'+str(round(position)-1)+'F'+str(application.ui.dial_FS.value())+'\n'))
                    s.write(str.encode('$J=X'+str(round(position)-5)+'F'+str(application.ui.dial_FS.value())+'\n'))
                    application.ui.spinBox_position.setValue(int(position))
                
            if close_everything == 1:
                s.close()
                return 0


    return 0

############################################################################
############################################################################

############################################################################
############################################################################

def init_graph():
    #time.sleep(3)

    print("Starting Graphs")
 
    application.ui.graphicsView.showGrid(x=True,y=True)
    application.ui.graphicsView.setXRange(0,8)
    application.ui.graphicsView.setYRange(25,225)
    application.ui.graphicsView.setMouseEnabled(x=False, y=False)
    application.ui.graphicsView.plot([0,8],[183,183], pen='m')


def reinit_graph():
    application.ui.graphicsView.clear()
    application.ui.graphicsView.plot([0,8],[183,183], pen='m')

############################################################################
############################################################################

def reflow_app():
    global oven_state
    global temp_0
    global temp_0_rate
    global Button_Start_pressed
    global command_transfer
    global cycle_started
    timer1= time.time()
    
    speed = 1850

    #Controls temperature rate. 
    #######################################
    pid_rate1 = PID(3, 0.01, 0.1, setpoint=1)
    pid_rate1.output_limits = (-5, 5)
    pid_rate1.proportional_on_measurement = False
    pid_rate1_F = 100
    pid_rate1_max = 0
    pid_rate1_min = 730
    #######################################
    #Controls the actual temperature of soaking time
    pid_temp1= PID(.5, 0.01, 0.2, setpoint=140)
    pid_temp1.output_limits = (-2, .5)
    pid_temp1.proportional_on_measurement = False
    pid_temp1_F = 100
    timer_soak= time.time() #30-90 seconds 30-120 acceptable 
    #######################################
    #Controls the actual temperature of soaking time
    pid_rate2= PID(1.3, 0.02, 0.2, setpoint=.6)
    pid_rate2.output_limits = (-5, 5)
    pid_rate2.proportional_on_measurement = False
    pid_rate2_F = 100
    timer_dripping= time.time() #30-90 seconds 30-120 acceptable 
    #######################################
    #Timestamps
    TimeAboveLiquidus = .07 #Also used to time the reflow 45-60 seconds
    Soak_last_pos = 0

    pid_dt = time.time()

    QThread.msleep(3000)
    application.ui.label_test.setText(f"State: 0. Ready.")

    while 1: 
        #First wait for the start button
        #Then start the sequence 
        #either use the preheat zone and prewarm to 100
        #Then go to the critical zone (my cabezone) 
        #When there use the 
        QThread.msleep(50)
        pid_dt =time.time()-timer1
        if (time.time()-timer1) > 1000/1000:
            timer1 = time.time()
            #print(timer1)
            temp = temp_0 

            #application.ui.label_test.setText(f"State: {oven_state}")

            ###########################################################
            if oven_state == 0:
            ###########################################################
                application.ui.label_test.setText(f"State: 0. Ready.")

                if Button_Start_pressed == 1:
                    Button_Start_pressed = 0
                    reinit_graph()
                    new_position = application.ui.spinBox_preheat.value()
                    print(f"Oven program started, Position preheat: {new_position} Speed {speed}")
                    print(str.encode('G1X'+str(new_position)+'F'+str(speed)+'\n'))
                    command_transfer = 'G1X'+str(new_position)+'F'+str(speed)+'\n'
                    application.ui.label_test.setText(f"State: 1 : Preheating")
                    oven_state = 1
                    global cycle_started
                    cycle_started = True
            ###########################################################
            elif oven_state == 1: #Preheat
            ###########################################################
                application.ui.label_test.setText(f"State: 1 : Preheating: {(60-temp):,.2f}")

                if temp > 60:
                    oven_state = 2
                    new_position = application.ui.spinBox_critical.value()
                    print(f"Moving to critical point: {new_position} Speed {speed}")
                    print(str.encode('G1X'+str(new_position)+'F'+str(speed)+'\n'))
                    command_transfer = 'G1X'+str(new_position)+'F'+str(speed)+'\n'
            ###########################################################


            elif oven_state == 2: #Waiting to arrive to critical zone 
            ###########################################################
                new_position = application.ui.spinBox_critical.value() 
                application.ui.label_test.setText(f"State: 2 : Moving to Critical {(new_position-position):,.2f}mm")
                if position >= new_position-2: #waiting until we arrive to new location.. 
                    oven_state = 3
                    print("Arrived to Critical point")
                    application.ui.label_test.setText(f"State: 2 : Arrived!")
            ###########################################################
            elif oven_state == 3: #Increasing temp to 135 at 1C/s (to SoakZone)
            ###########################################################
                #warming from Preheat to Soaking between 140-150C, 130-170C Acceptable.  
                #Here we will use a PID loop jog to the desired value (130C) at rate <2C/s 
                #After the that is achieve we will just to the next loop. 
                """Add PID loop here"""
                pid_rate1.sample_time = pid_dt
                output = pid_rate1(temp_0_rate) #<-----------------------------------------------
                command_transfer = 'G1X'+str(int(position+output))+'F'+str(pid_rate1_F)+'\n'
                print("PID Rate 1 output:",output)
                application.ui.label_test.setText(f"State: 3 : Heating to soaking T-0= {(130-temp):,.2f} PID {output:,.2f}")
                Soak_last_pos = position+output
                if temp > 130:
                    oven_state = 4
                    print("Temp of 130 reached")
                    timer_soak= time.time()
                    application.ui.label_test.setText(f"State: 3 : Arrived to SoakZone!")
                    pid_temp1.set_auto_mode(True, last_output=0)
            ###########################################################
            elif oven_state == 4: #Soaking stage. 45-60s Recommended. 30-100s Acceptable
            ###########################################################
                #Here the setpoing is changed to maintain the temp between 140-150 using PWM value
                #When the timer is done 
                """Cascade PID loop"""
                pid_temp1.sample_time = pid_dt
                output = pid_temp1(temp_0) #<-----------------------------------------------

                pid_rate1.setpoint = output 
                pid_rate1.sample_time = pid_dt
                output2 = pid_rate1(temp_0_rate) #<-----------------------------------------------
                if position+output2 > 730:
                    command_transfer = 'G1X'+str(int(position+output2))+'F'+str(pid_rate1_F)+'\n'

                #command_transfer = 'G1X'+str(int(position+output))+'F'+str(pid_temp1_F)+'\n'
                #print(f"PID Temp 1 {output:,.2f}, T-0 = {(time.time() - timer_soak):,.2f}")
                application.ui.label_test.setText(f"State: 4 : Soaking: t-0 = {45-(time.time() - timer_soak):,.2f} PID{output:,.2f}->{output2:,.2f}")

                if time.time() - timer_soak > 45: #45 seconds? 
                    oven_state = 5
                    application.ui.label_test.setText(f"State: 4 : Timeout!")
                    command_transfer = 'G1X'+str(Soak_last_pos)+'F'+str(pid_rate1_F)+'\n'
            ###########################################################
            elif oven_state == 5: #Here we slowly move the car at rate of .5-1Cs recommend up to 2.4C/s is acceptable. 
            ###########################################################
                """Add PID loop here"""
                pid_rate2.sample_time = pid_dt
                output = pid_rate2(temp_0_rate) #<-----------------------------------------------
                command_transfer = 'G1X'+str(int(position+output))+'F'+str(pid_rate2_F)+'\n'
                print("PID Rate 2 output:",output)
                application.ui.label_test.setText(f"State: 5 : Heating to Peak t-0= {(210-temp):,.2f} PID {output:,.2f}")

                if temp >= 183:
                    if TimeAboveLiquidus == .07: #just to know we haven't been here
                        TimeAboveLiquidus = time.time()
                        print("###Warning above liquidus temp!###")
                        pid_rate2.setpoint = 1.2
                        pid_rate2.Ki = .1

                if temp > 210: 
                    oven_state = 6
                    application.ui.label_test.setText(f"State: 5 : Done!")
                    new_position = application.ui.spinBox_maxTravel.value()
                    print(str.encode('G1X'+str(new_position)+'F'+str(speed)+'\n'))
                    command_transfer = 'G1X'+str(new_position)+'F'+str(speed)+'\n'
                    #maybe stop the car just in case
            ###########################################################
            elif oven_state == 6: #here we just move the car to the reflow position and wait. 
            ###########################################################
                #We wait around 30-60 seconds... 
                application.ui.label_test.setText(f"State: 6 : reflowing t-0= {30-(time.time() - TimeAboveLiquidus):,.2f}")

                if time.time() - TimeAboveLiquidus > 30:
                    oven_state = 7
                    new_position = application.ui.spinBox_dripping.value()
                    print(str.encode('G1X'+str(new_position)+'F'+str(speed)+'\n'))
                    command_transfer = 'G1X'+str(new_position)+'F'+str(speed)+'\n'
                    application.ui.label_test.setText(f"State: 7 : dripping")
                #send the command to the dripping position. 
            ###########################################################
            elif oven_state == 7: #Here we waiting until we arrive to the dripping 
            ###########################################################
                new_position = application.ui.spinBox_dripping.value()
                #We wait around 30-60 seconds... 
                application.ui.label_test.setText(f"State: 7 : Waiting for drip... Moving?->{abs(position - new_position)}")

                if abs(position - new_position) < 11: #waiting until we arrive to new location.. 
                    oven_state = 3
                    print("Arrived to dripping")
                    application.ui.label_test.setText(f"State: 7 : Arrived to dripping!")
                    oven_state = 8
                    timer_dripping= time.time()
            ###########################################################
            elif oven_state == 8: #here we just move the car to the reflow position and wait. 
            ###########################################################
                application.ui.label_test.setText(f"State: 8 : Dripping t-O : {time.time() - timer_dripping:,.2f}")
                #We wait around 15 seconds... 
                if time.time() - timer_dripping > 25: 
                    oven_state = 9
                    application.ui.label_test.setText(f"State: 8 : Timeout!")
                    new_position = application.ui.spinBox_coolDown.value()
                    command_transfer = 'G1X'+str(new_position)+'F'+str(speed)+'\n'
            ###########################################################
            elif oven_state == 9: #Here we waint until it cools down to <80
            ###########################################################
                
                application.ui.label_test.setText(f"State: 9 : Cooling down {(80-temp):,.2f}")
                if temp < 80:
                    application.ui.label_test.setText(f"State: 9 : Cool down completed! DONE!")
                    oven_state = 0
                    cycle_started = False
                    new_position = application.ui.spinBox_home.value()
                    command_transfer = 'G1X'+str(new_position)+'F'+str(speed)+'\n'
                #we Finish save data whatever and send card to home. 

        if close_everything == 1:
            return 0
    
    

############################################################################
############################################################################


def inits():

    global command_transfer 
    command_transfer = None
    #set_Setting("option1", "test2")
    #get_Setting("option1")
    application.ui.comboBox_stepper_ports.addItem("Select COM")
    application.ui.comboBox_temp_ports.addItem("Select COM")
    #Loading default settings
    if get_Setting("maxFS") != None:
        value = get_Setting("maxFS")
        application.ui.spinBox_maxFS.setValue(value)
        application.ui.dial_FS.setMaximum(value)

    t1 = threading.Thread(target=stepper_port)
    t1.start()

    t2 = threading.Thread(target=temp_port)
    t2.start()

    t3 = threading.Thread(target=reflow_app)
    t3.start()

    init_graph()

    #t3 = threading.Thread(target=graph_control)
    #t3.start()


############################################################################
############################################################################


if __name__ == "__main__":
    #global getParams_requested
    
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    inits() 
    #stepper_port()
    timer = QTimer()
    timer.timeout.connect(lambda: None)
    timer.start(100)
    sys.exit(app.exec())


    

