import os
import serial
import time   
os.system ("sudo pigpiod") 
time.sleep(1) 
import pigpio 

ESC=4

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0) 

max_value = 1610 
min_value = 1000

def calibrate():   #This is the auto calibration procedure of a normal ESC
    pi.set_servo_pulsewidth(ESC, 0)
    print("Disconnect the battery and press Enter")
    inp = raw_input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC, max_value)
        print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
        inp = raw_input()
        if inp == '':            
            pi.set_servo_pulsewidth(ESC, min_value)
            print "Wierd eh! Special tone"
            time.sleep(7)
            print "Wait for it ...."
            time.sleep (5)
            print "Im working on it, DONT WORRY JUST WAIT....."
            pi.set_servo_pulsewidth(ESC, 0)
            time.sleep(2)
            print "Arming ESC now..."
            pi.set_servo_pulsewidth(ESC, min_value)
            time.sleep(1)
            print "See.... uhhhhh"
            ser = serial.Serial('/dev/ttyUSB0', 9600,timeout = .15)
            while True:
                response = ser.readline().strip()
                data = response.decode("utf-8")
                if (data != ""):
                    speed_data = int(data)
                    print(speed_data)
                    print(type(speed_data))
                    pi.set_servo_pulsewidth(ESC, speed_data)
                        
            
calibrate()

    