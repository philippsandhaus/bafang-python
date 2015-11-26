# bafang-python
This is an attempt to decipher the protocol which is used by Bafang Pedelec Motors like BBS01 or BBS02 and provide a python tool/library to communicate with these devices.

This is a description of the reverse-engineered Bafang protocol. If not stated otherwise, all values have to be interpreted as hex values.

Baudrate: 1200,8,N,1


## Command: Connect
* **Send:** 11 51 04 B0 05  (05 = (51 + 04 + B0) MOD 256)
* **Response:** 51 10 48 5A 58 54 53 5A 5A 36 32 32 32 30 31 31 01 14 1B

### Response (description):

* 00: 51 
* 01: 10
* 02-05: Manufacturer in ASCII (48 5A 58 54 -> HZXT)
* 06-09: Model in ASCII (53 5A 5A 36 -> SZZ6)
* 10-11: HW Version in ASCII {10}.{11} (32 32 -> 2.2)
* 12-15: FW Version in ASCII {12}.{13}.{14}.{15} (32 30 31 31 -> 2.0.1.1)
* 16: Voltage
    * 00: 24V (18-22)
    * 01: 36V (28-32)
    * 02: 48V (38-43)
    * 03: 60V (48-55)
    * 04: 24V-48V (18-43)
    * else: 24V-60V (18-55)
* 17: Max Current (14 -> 20)
* 18: Checksum ? (1B)


## Command: Read Basic

* **Send:** 11 52
* **Response:** 52 18 1F 0F 00 1C 25 2E 37 40 49 52 5B 64 64 64 64 64 64 64 64 64 64 64 34 01 DF

### Response (description):

* 00: 52 
* 01: 18 
* 02: Low Battery Protect (V) (1F -> 31)
* 03: Limited Current (A) (0F -> 15) 
* 04: Limit Current (%) Assist0 (00 -> 0) 
* 05: Limit Current (%) Assist1 (1C -> 28) 
* 06: Limit Current (%) Assist2 (25 -> 37)
* 07: Limit Current (%) Assist3 (2E -> 46) 
* 08: Limit Current (%) Assist4 (37 -> 55)
* 09: Limit Current (%) Assist5 (40 -> 64)
* 10: Limit Current (%) Assist6 (49 -> 75) 
* 11: Limit Current (%) Assist7 (52 -> 82) 
* 12: Limit Current (%) Assist8 (5B -> 91) 
* 13: Limit Current (%) Assist9 (64 -> 100) 
* 14: Limit Speed (%) Assist0 (64 -> 100) 
* 15: Limit Speed (%) Assist1 (64 -> 100) 
* 16: Limit Speed (%) Assist2 (64 -> 100) 
* 17: Limit Speed (%) Assist3 (64 -> 100) 
* 18: Limit Speed (%) Assist4 (64 -> 100)
* 19: Limit Speed (%) Assist5 (64 -> 100)
* 20: Limit Speed (%) Assist6 (64 -> 100) 
* 21: Limit Speed (%) Assist7 (64 -> 100)
* 22: Limit Speed (%) Assist8 (64 -> 100)
* 23: Limit Speed (%) Assist9 (64 -> 100)
* 24: Wheel Diameter (Inch) (34 -> 52) 
	10-1E: Diameter in Inch
s:=redata[24];
t:=s mod 2;
n:=s div 2;
m:=t+n;
if (m>27) then
begin
 if (m=28) and (t=1) then
   ComboBox4.ItemIndex:=12
 else
   ComboBox4.ItemIndex:=m-15;
 end
else
 ComboBox4.ItemIndex:=m-16;

* 25: Speedmeter Model/Speedmeter Signal 01
s:=redata[25];
t:=s mod 64;
n:=s div 64;
if n=3 then
   ComboBox5.ItemIndex:=2
else
   ComboBox5.ItemIndex:=n;
Edit22.Text:=inttostr(t);

* 26: Checksum? DF

## Command: Read Pedal
* **Send:** 11 53
* **Response:** 53 0B 03 FF FF 64 06 14 0A 19 08 14 14 27

### Response (description):
* 00: 53 
* 01: 0B 
* 02: Pedal Type (03)
    * 00: None
    * 01: DH-Sensor-12
    * 02: BB-Sensor-32
    * 03: DoubleSignal-24
* 03: Designated Assist (FF)
    * 00-09: Assist Mode No.
    * FF: By Display's Command
* 04: Speed Limit (FF)
    * 0F-28: Speed Limit in km/h
    * FF: By Display's Command
* 05: Start current in % (64 -> 100) 
* 06: Slow-Start Mode (06 -> 6)
    * 01-08: Mode Number
* 07: Startup Degree (Signal No.) (14 -> 20)
    * Integer: Number of Signal before start
* 08: Work Mode (0A -> 10)
    * 0A-50: Angular Speed of pedal/wheel*10
    * FF: Undetermined
* 09: Time of Stop (19 -> 25)
    * Integer: *10ms
* 10: Current Decay (08 -> 8)
    * 01-08: Current Decay 
* 11: Stop Decay (14 -> 20)
    * Integer: *10ms
* 12: Keep Current in % (14 -> 20)
* 13: Checksum ? (27)

## Command: Read Throttle
* **Send:** 11 54
* **Response:** 54 06 0B 23 00 03 14 AC

### Response (description):
* 00: 54
* 01: 06
* 02: Start Voltage *100mv (0B -> 11)
* 03: End Voltage *100mv (23 -> 35)
* 04: Mode
    * 00: Speed
    * 01: Current
* 05: Designated Assist (03 -> 3)
    * 00-09: Assist Mode No.
    * FF: By Display's Command
* 06: Speed Limited (14 - 20)
    * 0F-28: Speed Limit in km/h
    * FF: By Display's Command
* 07: Start Current in % (AC ?????)
	
## Command: Set Basic
* **Send:** ????
* **Response:** 52 24

### Response (description):
* 00: 52
* 01: Result Code
    * 00: Low Battery Protect Setting Error
    * 01: Limited Current Setting Error
    * 02: Limit Current Assist0 Error
    * 03: Limit Current Assist1 Error
    * 04: Limit Current Assist2 Error
    * 05: Limit Current Assist3 Error
    * 06: Limit Current Assist4 Error
    * 07: Limit Current Assist5 Error
    * 08: Limit Current Assist6 Error
    * 09: Limit Current Assist7 Error
    * 0A: Limit Current Assist8 Error
    * 0B: Limit Current Assist9 Error
    * 0C: Limit Speed Assist0 Error
    * 0D: Limit Speed Assist1 Error
    * 0E: Limit Speed Assist2 Error
    * 0F: Limit Speed Assist3 Error
    * 10: Limit Speed Assist4 Error
    * 11: Limit Speed Assist5 Error
    * 12: Limit Speed Assist6 Error
    * 13: Limit Speed Assist7 Error
    * 14: Limit Speed Assist8 Error
    * 15: Limit Speed Assist9 Error	
    * 16: Speedmeter Setting Error
    * 17: Speedmeter Signal Setting Error
    * 18: Success 
