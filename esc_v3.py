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

def calibrate():   #Normal bir ESC icin otomatik kalibrasyon fonksiyonudur.
    pi.set_servo_pulsewidth(ESC, 0)
    print("Bataryayı çıkarın ve Enter'a basin.")
    inp = raw_input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC, max_value)
        print("Bataryayı takin ve Enter'a basin.")
        inp = raw_input()
        if inp == '':            
            pi.set_servo_pulsewidth(ESC, min_value)
            print "Ozel tonda bir ses gelmeli."
            time.sleep(7)
            print "Biraz bekleyin..."
            time.sleep (5)
            print "Endiselenme :) Calisiyorum..."
            pi.set_servo_pulsewidth(ESC, 0)
            time.sleep(2)
            print "ESC simdi baslatiliyor."
            pi.set_servo_pulsewidth(ESC, min_value)
            time.sleep(1)
            print "------"
            '''
            XBee pc ye explorer ile baglandigindan seri okuma yapilmali.
            '''
            ser = serial.Serial('/dev/ttyUSB0', 9600,timeout = .15)  
            while True:
                response = ser.readline().strip()
                data = response.decode("utf-8")
                if (data != ""):  #Data kaybolmasina karsi onlem
                    speed_data = int(data)
                    #print(speed_data)
                    #print(type(speed_data))
                    pi.set_servo_pulsewidth(ESC, speed_data) 
                        
            
calibrate()
'''
While True dongusu son kisma alininca hatalar alindigi icin kalibre fonksiyonu icine yazildi.
'''

    