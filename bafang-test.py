import serial,time
from construct import *
from protocol import *

ser = serial.Serial('/dev/tty.usbserial-DJ005O71', 1200, timeout=1)
print(ser.name)

def read_config(cm, answ_format):
    #print cm.encode('hex')
    ser.write(cm)
    ser.flush()
    time.sleep(1)
    answ = ser.read(100)
    print answ.encode('hex')
    #t = answ_format.parse(answ)
    #print(t)

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
