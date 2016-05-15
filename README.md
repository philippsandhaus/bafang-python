# bafang-python
This is an attempt to decipher the protocol which is used by Bafang Pedelec Motors like BBS01 or BBS02 and provide a python tool/library to communicate with these devices.

This is a description of the reverse-engineered Bafang protocol. If not stated otherwise, all values have to be interpreted as hex values.

Baudrate: 1200,8,N,1


## Command: Connect
* **Send:** 0x11 0x51 0x04 0xB0 0x05  (0x05 = (0x51 + 0x04 + 0xB0) MOD 256)
* **Response:** 0x51 0x10 0x48 0x5A 0x58 0x54 0x53 0x5A 0x5A 0x36 0x32 0x32 0x32 0x30 0x31 0x31 0x01 0x14 0x1B

### Response (description):

* 00: 0x51 
* 01: 0x10 (Length?)
* 02-05: Manufacturer in ASCII (0x48 0x5A 0x58 0x54 -> HZXT)
* 06-09: Model in ASCII (0x53 0x5A 0x5A 0x36 -> SZZ6)
* 10-11: HW Version in ASCII {10}.{11} (0x32 0x32 -> 2.2)
* 12-15: FW Version in ASCII {12}.{13}.{14}.{15} (0x32 0x30 0x31 0x31 -> 2.0.1.1)
* 16: Voltage
    * 0x00: 24V (18-22)
    * 0x01: 36V (28-32)
    * 0x02: 48V (38-43)
    * 0x03: 60V (48-55)
    * 0x04: 24V-48V (18-43)
    * else: 24V-60V (18-55)
* 17: Max Current (0x14 -> 20)
* 18: Checksum ? (0x1B)


## Command: Read Basic

* **Send:** 0x11 0x52
* **Response:** 0x52 0x18 0x1F 0x0F 0x00 0x1C 0x25 0x2E 0x37 0x40 0x49 0x52 0x5B 0x64 0x64 0x64 0x64 0x64 0x64 0x64 0x64 0x64 0x64 0x64 0x34 0x01 0xDF

### Response (description):

* 00: 0x52 
* 01: 0x18 (Length?)
* 02: Low Battery Protect (V) (0x1F -> 31)
* 03: Limited Current (A) (0x0F -> 15) 
* 04: Limit Current (%) Assist0 (0x00 -> 0) 
* 05: Limit Current (%) Assist1 (0x1C -> 28) 
* 06: Limit Current (%) Assist2 (0x25 -> 37)
* 07: Limit Current (%) Assist3 (0x2E -> 46) 
* 08: Limit Current (%) Assist4 (0x37 -> 55)
* 09: Limit Current (%) Assist5 (0x40 -> 64)
* 10: Limit Current (%) Assist6 (0x49 -> 75) 
* 11: Limit Current (%) Assist7 (0x52 -> 82) 
* 12: Limit Current (%) Assist8 (0x5B -> 91) 
* 13: Limit Current (%) Assist9 (0x64 -> 100) 
* 14: Limit Speed (%) Assist0 (0x64 -> 100) 
* 15: Limit Speed (%) Assist1 (0x64 -> 100) 
* 16: Limit Speed (%) Assist2 (0x64 -> 100) 
* 17: Limit Speed (%) Assist3 (0x64 -> 100) 
* 18: Limit Speed (%) Assist4 (0x64 -> 100)
* 19: Limit Speed (%) Assist5 (0x64 -> 100)
* 20: Limit Speed (%) Assist6 (0x64 -> 100) 
* 21: Limit Speed (%) Assist7 (0x64 -> 100)
* 22: Limit Speed (%) Assist8 (0x64 -> 100)
* 23: Limit Speed (%) Assist9 (0x64 -> 100)
* 24: Wheel Diameter (Inch) (0x34)
    * 0x1F,0x20: 16"
    * 0x21,0x22: 17"
    * 0x23,0x24: 18"
    * 0x25,0x26: 19"
    * 0x27,0x28: 20"
    * 0x29,0x2A: 21"
    * 0x2B,0x2C: 22"
    * 0x2D,0x2E: 23"
    * 0x2F,0x30: 24"
    * 0x31,0x32: 25"
    * 0x33,0x34: 26"
    * 0x35,0x36: 27"
    * 0x37: 700C
    * 0x38: 28"
    * 0x39,0x3A: 29"
    * 0x3B,0x3C: 30"
* 25: Speedmeter Model/Speedmeter Signal 01
	* Bits 1-2 (Model)
		* 00: External
		* 01: Internal
		* 10: Motorphase
	* Bits 3-6 (Speedmeter Signals)
* 26: Checksum? 0xDF

## Command: Read Pedal
* **Send:** 0x11 0x53
* **Response:** 0x53 0x0B 0x03 0xFF 0xFF 0x64 0x06 0x14 0x0A 0x19 0x08 0x14 0x14 0x27

### Response (description):
* 00: 0x53 
* 01: 0x0B (Length?)
* 02: Pedal Type (0x03)
    * 0x00: None
    * 0x01: DH-Sensor-12
    * 0x02: BB-Sensor-32
    * 0x03: DoubleSignal-24
* 03: Designated Assist (FF)
    * 0x00-0x09: Assist Mode No.
    * 0xFF: By Display's Command
* 04: Speed Limit (FF)
    * 0x0F-0x28: Speed Limit in km/h
    * 0xFF: By Display's Command
* 05: Start current in % (0x64 -> 100)
    * 0x00-0x64
* 06: Slow-Start Mode (06 -> 6)
    * 0x01-0x08: Mode Number
* 07: Startup Degree (Signal No.) (0x14 -> 20)
    * Integer: Number of Signal before start
* 08: Work Mode (0x0A -> 10)
    * 0x0A-0x50: Angular Speed of pedal/wheel*10
    * 0xFF: Undetermined
* 09: Time of Stop (0x19 -> 25)
    * Integer: *10ms
* 10: Current Decay (0x08 -> 8)
    * 0x01-0x08: Current Decay 
* 11: Stop Decay (0x14 -> 20)
    * Integer: *10ms
* 12: Keep Current in % (0x14 -> 20)
* 13: Checksum ? (0x27)

## Command: Read Throttle
* **Send:** 0x11 0x54
* **Response:** 54 06 0B 23 00 03 11 14 AC

### Response (description):
* 00: 0x54
* 01: 0x06 (Length?)
* 02: Start Voltage *100mv (0x0B -> 11)
* 03: End Voltage *100mv (0x23 -> 35)
* 04: Mode
    * 0x00: Speed
    * 0x01: Current
* 05: Designated Assist (0x03 -> 3)
    * 0x00-0x09: Assist Mode No.
    * 0xFF: By Display's Command
* 06: Speed Limited (14 - 20)
    * 0x0F-0x28: Speed Limit in km/h
    * 0xFF: By Display's Command
* 07: Start Current in % (14 - 20)
* 08: Checksum ? (0xAC)
	
## Command: Set Basic
* **Send:** 0x16 0x52 0x24 3..26 
* **Response:** 0x52 0x24

### Response (description):
* 00: 0x52
* 01: Result Code
    * 0x00: Low Battery Protect Setting Error
    * 0x01: Limited Current Setting Error
    * 0x02: Limit Current Assist0 Error
    * 0x03: Limit Current Assist1 Error
    * 0x04: Limit Current Assist2 Error
    * 0x05: Limit Current Assist3 Error
    * 0x06: Limit Current Assist4 Error
    * 0x07: Limit Current Assist5 Error
    * 0x08: Limit Current Assist6 Error
    * 0x09: Limit Current Assist7 Error
    * 0x0A: Limit Current Assist8 Error
    * 0x0B: Limit Current Assist9 Error
    * 0x0C: Limit Speed Assist0 Error
    * 0x0D: Limit Speed Assist1 Error
    * 0x0E: Limit Speed Assist2 Error
    * 0x0F: Limit Speed Assist3 Error
    * 0x10: Limit Speed Assist4 Error
    * 0x11: Limit Speed Assist5 Error
    * 0x12: Limit Speed Assist6 Error
    * 0x13: Limit Speed Assist7 Error
    * 0x14: Limit Speed Assist8 Error
    * 0x15: Limit Speed Assist9 Error	
    * 0x16: Speedmeter Setting Error
    * 0x17: Speedmeter Signal Setting Error
    * 0x18: Success 

## Command: Set Pedal
* **Send:** 0x16 0x53 0x11 3..13 14(Checksum)
* **Response:** 0x53 0x24

### Response (description):
* 00: 0x53
* 01: Result Code (TODO) 
    * 0x00: Low Battery Protect Setting Error
    * 0x01: Limited Current Setting Error
    * 0x02: Limit Current Assist0 Error
    * 0x03: Limit Current Assist1 Error
    * 0x04: Limit Current Assist2 Error
    * 0x05: Limit Current Assist3 Error
    * 0x06: Limit Current Assist4 Error
    * 0x07: Limit Current Assist5 Error
    * 0x08: Limit Current Assist6 Error
    * 0x09: Limit Current Assist7 Error
    * 0x0A: Limit Current Assist8 Error
    * 0x0B: Limit Current Assist9 Error
    * 0x0C: Limit Speed Assist0 Error
    * 0x0D: Limit Speed Assist1 Error
    * 0x0E: Limit Speed Assist2 Error
    * 0x0F: Limit Speed Assist3 Error
    * 0x10: Limit Speed Assist4 Error
    * 0x11: Limit Speed Assist5 Error
    * 0x12: Limit Speed Assist6 Error
    * 0x13: Limit Speed Assist7 Error
    * 0x14: Limit Speed Assist8 Error
    * 0x15: Limit Speed Assist9 Error	
    * 0x16: Speedmeter Setting Error
    * 0x17: Speedmeter Signal Setting Error
    * 0x18: Success 
