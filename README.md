# pilogger
Repository for keeping info on my Raspberry Pi that is going to be launched in a rocket

# pins
Left side |pins |  right side
--------- | ----|---------
3.3v |1  ○ ○ 2|5v from regulator
SDA  |3  ○ ○ 4|empty 5v
SCL   |5  ○ ○ 6|ground to regulator
. |7 ○ ○ 8 |GPIO 14 
ground for MPU |9  ○ ○ 10|GPIO 15: accel reading light, green wire, yellow LED
 .|11 ○ ○ 12|GPIO 18: running light, yellow wire, purple LED
 .|13 ○ ○ 14 |Ground for LEDs
 .|15 ○ ○ 16 |GPIO 23
 .|17 ○ ○ 18 |GPIO 24
 .|19 ○ ○ 20 |Ground
 .|21 ○ ○ 22| 
 .|23 ○ ○ 24| 
 .|25 ○ ○ 26| 
 .|27 ○ ○ 28|  
 .|29 ○ ○ 30| 
 .|31 ○ ○ 32| 
 .|33 ○ ○ 34| 
 .|35 ○ ○ 36| 
 .|37 ○ ○ 38| 
 .|39 ○ ○ 40| 

#power draw test
Very rough approximation, sorry for not doing this in amps
Start from boot: 8.27v
at 8 mins : 8.12 v
at 12 . in: 8.08 v

time period 1: 0.01875 v/min
time period 2: 0.0100  v/min

empty is 7 volts, full is 8.4
1.4 volts/(0.15 v/min) = 93.3 minutes
