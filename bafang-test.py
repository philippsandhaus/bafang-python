import serial,time
from construct import *
from protocol import *
import sys
import glob


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

ser = serial.Serial('/dev/tty.usbserial-DJ005O71', 1200, timeout=1)
#ser = serial.Serial(serial_ports()[0], 1200, timeout=1)
print(ser.name)

def read_config(cm, answ_format):
    print cm.encode('hex')
    ser.write(cm)
    ser.flush()
    time.sleep(1)
    answ = ser.read(100)
    print answ.encode('hex')
    t = answ_format.parse(answ)
    print(t)

read_config(connect_cmd.build(
        Container()), 
    info_message)

read_config(read_cmd.build(
        Container(command = 'BASIC')), 
    basic_message)

read_config(read_cmd.build(
        Container(command = 'PEDAL')), 
    pedal_message)

read_config(read_cmd.build(
        Container(command = 'THROTTLE')), 
    throttle_message)

    
ser.close()    
