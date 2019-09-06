import sys, os, platform, pty, time, threading, glob, json
import serial
import serial.tools.list_ports


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    #print(sys.platform)
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        #ports = glob.glob('/dev/tty[A-Za-z]*')
        ports = glob.glob('/dev/ttyUSB*')
    elif sys.platform.startswith('darwin'):
        #ports = glob.glob('/dev/tty.*')
        ports = glob.glob('/dev/cu*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            #print("reading ports", port)
            #s1 = serial.Serial(port)
            #s1.close()
            result.append(port)
            time.sleep(100/1000)
        except (OSError, serial.SerialException):
            pass
    return result

def set_Setting(elsetting, elvalue =''):
    config = {'': ''}
    try:
        with open('settings.txt', 'r+') as f:
            config = json.load(f)       
        #print("The current data is: ", config)
        if elsetting in config:
            print(f'The {elsetting!r} changed from {config[elsetting]!r} to {elvalue!r}')
            #edit the data
            config[elsetting] = elvalue
            #write it back to the file
            with open('settings.txt', 'w') as f:
                json.dump(config, f)
        else:
            print(f'Key {elsetting!r} data is not availble!!! Adding it')
            with open('settings.txt', 'r+') as f:
                new_dict = ({elsetting: elvalue})
                config.update(new_dict)
                json.dump(config,f)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        with open('settings.txt', 'w') as f:
            json.dump(config, f)


def get_Setting(elsetting):
    config = {'': ''}
    try:
        with open('settings.txt', 'r+') as f:
            config = json.load(f)

        if elsetting in config:
            #returning the setting. 
            print(f'The {elsetting!r} is returning the value: {config[elsetting]!r}')
            return config[elsetting]
        else:
            return None
    except:
        print("Unexpected error:", sys.exc_info()[0])


    