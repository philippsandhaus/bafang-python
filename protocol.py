from construct import Const,Struct,Enum,Bytes,Byte,Array,BitStruct,BitsInteger

connect_cmd = Struct(
    'connect_cmd' / Const(b"\x11\x51\x04\xB0\x05")
)


read_cmd = Struct(
    'read_cmd' / Const(b"\x11"), # read command
    'command' / Enum(Byte,
        BASIC = 0x52,
        PEDAL = 0x53,
        THROTTLE = 0x54)
)

write_cmd = Struct(
        'write_cmd' / Const(b"\x16"), # write command
        'command' / Enum(Byte,
            BASIC = 0x52,
            PEDAL = 0x53,
            THROTTLE = 0x54),
        'data_length' / Byte,
        'data' / Bytes(5)
    )
    #Enum(Integer('data_length'),
    #    BASIC = 24,
    #    PEDAL = 11,
    #    THROTTLE = 6)


# 51 10 48 5a 58 54 53 5a 5a 36 32 32 32 30 31 31 01 14 1b
info_message = Struct(
    'info_message' / Byte,
    'status' / Byte,
    'manufacturer' / Bytes(4),
    'model' / Bytes(4),
    'HW-Version' / Bytes(2),
    'FW-Version' / Bytes(4),
    'Voltage' / Enum(Byte,
        VOLTAGE_24 = 0x00,
        VOLTAGE_36 = 0x01,
        VOLTAGE_48 = 0x02,
        VOLTAGE_60 = 0x03,
        VOLTAGE_24_48 = 0x04,
        VOLTAGE_24_60 = 0x05
    ),
    'max_current' / Byte,
    'checksum' / Byte
)

basic_message = Struct(
    'basic_message' / Const(b"\x52\x18"),
    'low_battery_protect' / Byte,
    'limited_current' / Byte,
    'limit_current_levels' / Array(10,Byte),
    'limit_speed_levels' / Array(10,Byte),
    'wheel_diameter' / Enum(Byte,
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
    'Speedmeter' / BitStruct(
      'Speedmeter_Model' / Enum(BitsInteger(2),
          EXTERNAL = 0b00,
          INTERNAL = 0b01,
          MOTORPHASE = 0b10
      ),
      'Signals' / BitsInteger(6)  
    ),
    'Checksum' / Byte
)

# 53 0b 03 ff ff 64 06 14 0a 19 08 14 14 27
pedal_message = Struct(
    'pedal_message' / Const(b"\x53\x0B"),
    'pedal_type' / Enum(Byte,
        NONE             = 0x00,
        DH_SENSOR_12     = 0x01,
        BB_SENSOR_32     = 0x02,
        DOUBLE_SIGNAL_24 = 0x03
    ),
    'designated_assist' / Enum(Byte,
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
    'speed_limit' / Byte,
    'start_current' / Byte,
    'slow_start_mode' / Byte,
    'startup_degree' / Byte,
    'work_mode' / Byte,
    'time_of_stop' / Byte,
    'current_decay' / Byte,
    'stop_decay' / Byte,
    'keep_current' / Byte,
    'Checksum' / Byte
)

# 54 06 0b 23 00 03 11 14 ac
throttle_message = Struct(
    'throttle_message' / Const(b"\x54\x06"),
    'start_voltage' / Byte, # x * 100mV
    'end_voltage' / Byte, # x * 100mV
    'mode' / Enum(Byte,
        SPEED   = 0x00,
        CURRENT = 0x01
    ),
    'designated_assist' / Enum(Byte,
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
    'speed_limited' / Byte,
    'start_current' / Byte,
    'Checksum' / Byte
)

