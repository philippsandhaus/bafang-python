from time import sleep
from serial import Serial, SerialException
from serial.tools.list_ports import comports
from construct import Const
from protocol import connect_cmd, read_cmd, info_message, basic_message, pedal_message, throttle_message


def serial_ports():
    """Lists serial port names using pyserial's built-in detection.

    Uses platform-specific APIs to enumerate serial ports efficiently,
    avoiding expensive trial-and-error port opening.

    :returns:
        A list of available serial port names
    :raises EnvironmentError:
        If no serial ports are found
    """
    ports = [port.device for port in comports()]
    
    if not ports:
        raise EnvironmentError('No serial ports found')
    
    return ports


# Initialize serial connection
ser = Serial(serial_ports()[0], 1200, timeout=1)


def read_config(cm, answ_format):
    """Read configuration from device.
    
    :param cm: Command to send (bytes)
    :param answ_format: Format structure for parsing response
    """
    print(cm)
    ser.write(cm)
    ser.flush()
    sleep(1)
    answ = ser.read(100)
    print(answ)
    t = answ_format.parse(answ)
    print(t)


# Read configurations
read_config(connect_cmd.build(dict()), info_message)

read_config(read_cmd.build(dict(command='BASIC')), basic_message)

read_config(read_cmd.build(dict(command='PEDAL')), pedal_message)

read_config(read_cmd.build(dict(command='THROTTLE')), throttle_message)

ser.close()
