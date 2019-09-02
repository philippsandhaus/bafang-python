from time import sleep
from serial import Serial, SerialException
from construct import Const
from protocol import connect_cmd, read_cmd, info_message, basic_message, pedal_message, throttle_message
from sys import platform
from glob import glob


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif platform.startswith('linux') or platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob('/dev/tty[A-Za-z]*')
    elif platform.startswith('darwin'):
        ports = glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = Serial(port)
            s.close()
            result.append(port)
        except (OSError, SerialException):
            pass
    return result

#ser = serial.Serial('/dev/tty.usbserial-DJ005O71', 1200, timeout=1)
ser = Serial(serial_ports()[0], 1200, timeout=1)
#print(ser.name)

def read_config(cm, answ_format):
    print(cm)
    ser.write(cm)
    ser.flush()
    sleep(1)
    answ = ser.read(100)
    print(answ)
    t = answ_format.parse(answ)
    print(t)

read_config(connect_cmd.build(
        dict()), 
    info_message)

read_config(read_cmd.build(
        dict(command = 'BASIC')), 
    basic_message)

read_config(read_cmd.build(
        dict(command = 'PEDAL')), 
    pedal_message)

read_config(read_cmd.build(
        dict(command = 'THROTTLE')), 
    throttle_message)

ser.close()    
