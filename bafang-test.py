import serial,time

with serial.Serial('/dev/tty.usbserial-DJ005O71', 1200, timeout=1) as ser:
    print(ser.name)
    ser.write("\x11\x51\x04\xB0\x05")
    ser.flush()
    time.sleep(1)
    s = ser.read(100)
    print(s)
    
    ser.write("\x11\x52")
    ser.flush()
    time.sleep(1)
    s = ser.read(100)
    print(s)
    
    
    ser.write("\x11\x53")
    ser.flush()
    time.sleep(1)
    s = ser.read(100)
    print(s)
    
    
    ser.write("\x11\x54")
    ser.flush()
    time.sleep(1)
    s = ser.read(100)
    print(s)
    
    ser.close()
    
