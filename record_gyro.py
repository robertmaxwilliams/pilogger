#!/usr/bin/python
from __future__ import division

from gpiozero import LED, Button
import smbus
import math
import time

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)


bus = smbus.SMBus(1) # or bus = smbus.SMBus(0) for Revision 1 boards
address = 0x68       # This is the address value read via the i2cdetect command

# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)


#header line for each program run
with open("mpu_data.csv", "a") as myfile:
    myfile.write("\nGyro: x, y, z Accel: x, y, z, time\n")


status_led = LED(15)
print "reading mpu data"
while True:
    if int(time.time()*2)%2 == 0:
        status_led.off()
    else:
	status_led.on()
    gyro_xout = read_word_2c(0x43) / 131.0
    gyro_yout = read_word_2c(0x45) / 131.0
    gyro_zout = read_word_2c(0x47) / 131.0

    accel_xout = read_word_2c(0x3b) / 16384.0
    accel_yout = read_word_2c(0x3d) / 16384.0
    accel_zout = read_word_2c(0x3f) / 16384.0

    rotation_x = get_x_rotation(accel_xout, accel_yout, accel_zout)
    rotation_y = get_y_rotation(accel_xout, accel_yout, accel_zout)
    
    #data line to append to file
    dataline = str(gyro_xout)+", "+str(gyro_yout)+", "+str(gyro_zout)+", "+str(accel_xout)+", "\
        +str(accel_yout)+", "+str(accel_zout)+", "+str(rotation_x)+", "+str(rotation_y)+", "+str(time.time())+"\n"

    #save data to file
    with open("mpu_data.csv", "a") as myfile:
        myfile.write(dataline)

