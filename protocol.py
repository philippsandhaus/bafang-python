from construct import *

connect_cmd = Struct('connect',
    Magic('\x11\x51\x04\xB0\x05')
)


read_cmd = Struct('read',
    Magic('\x11'),
    Enum(Byte('command'),
        BASIC = 0x52,
        PEDAL = 0x53,
        THROTTLE = 0x54)
)

# 51 10 48 5a 58 54 53 5a 5a 36 32 32 32 30 31 31 01 14 1b
info_message = Struct('info',
    Byte('command'),
    Byte('status'),
    Bytes('manufacturer',4),
    Bytes('model',4),
    Bytes('HW-Version',2),
    Bytes('FW-Version',4),
    Enum(Byte('Voltage'),
        VOLTAGE_24 = 0x00,
        VOLTAGE_36 = 0x01,
        VOLTAGE_48 = 0x02,
        VOLTAGE_60 = 0x03,
        VOLTAGE_24_48 = 0x04,
        VOLTAGE_24_60 = Pass
    ),
    Byte('max_current'),
    Byte('checksum')
)

basic_message = Struct('basic',
    Magic('\x52\x18'),
    Byte('low_battery_protect'),
    Byte('limited_current'),
    Array(10,ULInt8('limit_current_levels')),
    Array(10,ULInt8('limit_speed_levels')),
    Enum(Byte('wheel_diameter'),
        INCH_16  = 0x1F,
        INCH_16a = 0x20,
        INCH_17  = 0x21,
        INCH_17a = 0x22,
        INCH_18  = 0x23,
        INCH_18a = 0x24,
        INCH_19  = 0x25,
        INCH_19a = 0x26,
        INCH_20  = 0x27,
        INCH_20a = 0x28,
        INCH_21  = 0x29,
        INCH_21a = 0x2A,
        INCH_22  = 0x2B,
        INCH_22a = 0x2C,
        INCH_23  = 0x2D,
        INCH_23a = 0x2E,
        INCH_24  = 0x2F,
        INCH_24a = 0x30,
        INCH_25  = 0x31,
        INCH_25a = 0x32,
        INCH_26  = 0x33,
        INCH_26a = 0x34,
        INCH_27 =  0x35,
        INCH_27a = 0x36,
        SIZE_700C = 0x37,
        INCH_28  = 0x38,
        INCH_28a = 0x39,
        INCH_29  = 0x3A,
        INCH_29a = 0x3B,
        INCH_30  = 0x3C,
        INCH_30a = 0x3D
    ),
    BitStruct('Speedmeter',
      Enum(BitField('Speedmeter_Model',2),
          EXTERNAL = 0b00,
          INTERNAL = 0b01,
          MOTORPHASE = 0b10
      ),
      BitField('Signals',6)  
    ),
    Byte('Checksum')
)

# 53 0b 03 ff ff 64 06 14 0a 19 08 14 14 27
pedal_message = Struct('pedal',
    Magic('\x53\x0B'),
    Enum(Byte('pedal_type'),
        NONE             = 0x00,
        DH_SENSOR_12     = 0x01,
        BB_SENSOR_32     = 0x02,
        DOUBLE_SIGNAL_24 = 0x03
    ),
    Enum(Byte('designated_assist'),
        MODE_0  = 0x00,
        MODE_1  = 0x01,
        MODE_2  = 0x02,
        MODE_3  = 0x03,
        MODE_4  = 0x04,
        MODE_5  = 0x05,
        MODE_6  = 0x06,
        MODE_7  = 0x07,
        MODE_8  = 0x08,
        MODE_9  = 0x09,
        DISPLAY = 0xFF
    ),
    Byte('speed_limit'),
    Byte('start_current'),
    Byte('slow_start_mode'),
    Byte('startup_degree'),
    Byte('work_mode'),
    Byte('time_of_stop'),
    Byte('current_decay'),
    Byte('stop_decay'),
    Byte('keep_current'),
    Byte('Checksum')
)

# 54 06 0b 23 00 03 11 14 ac
throttle_message = Struct('throttle',
    Magic('\x54\x06'),
    Byte('start_voltage'), # x * 100mV
    Byte('end_voltage'), # x * 100mV
    Enum(Byte('mode'),
        SPEED   = 0x00,
        CURRENT = 0x01
    ),
    Enum(Byte('designated_assist'),
        MODE_0  = 0x00,
        MODE_1  = 0x01,
        MODE_2  = 0x02,
        MODE_3  = 0x03,
        MODE_4  = 0x04,
        MODE_5  = 0x05,
        MODE_6  = 0x06,
        MODE_7  = 0x07,
        MODE_8  = 0x08,
        MODE_9  = 0x09,
        DISPLAY = 0xFF
    ),
    Byte('speed_limited'),
    Byte('start_current'),
    Byte('Checksum')
)

