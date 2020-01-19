# SDA = pin.SDA_1
# SCL = pin.SCL_1
# SDA_1 = pin.SDA
# SCL_1 = pin.SCL

from adafruit_servokit import ServoKit
import board
import busio
import time

import math

import keyboard


# On the Jetson Nano
# Bus 0 (pins 28,27) is board SCL_1, SDA_1 in the jetson board definition file
# Bus 1 (pins 5, 3) is board SCL, SDA in the jetson definition file
# Default is to Bus 1; We are using Bus 0, so we need to construct the busio first ...

print("Initializing Servos")
i2c_bus0=(busio.I2C(board.SCL_1, board.SDA_1))
print("Initializing ServoKit")
kit = ServoKit(channels=16, i2c=i2c_bus0)
# kit[0] is the bottom servo
# kit[1] is the top servo
print("Done initializing")

time.sleep(0.5)

i = 0
j = 0

tempo = 0.002
angleinc = 0.5

kit.servo[0].__init__
kit.servo[1].__init__

kit.servo[0].angle=0
kit.servo[1].angle=0

kit.servo[0].fraction = None
kit.servo[1].fraction = None

while True:
    
    if keyboard.is_pressed('a'):
            
            i = i + angleinc
         
            if i <= 170:
                
                kit.servo[0].angle=i
                kit.servo[0].fraction = None
          
                time.sleep(tempo)
            
            else :
                
                i= 170
                
    if keyboard.is_pressed('d'):
            
            i = i - angleinc
           
            
            time.sleep(tempo)
            
            if i >= 10 :
                
                kit.servo[0].angle=i
                kit.servo[0].fraction = None
            
                time.sleep(tempo)
            
            else :
            
                i = 10
                
    if keyboard.is_pressed('s'):
            
            j = j + angleinc
            
            if j <= 170:
                kit.servo[1].angle=j
                kit.servo[1].fraction = None
            
                time.sleep(tempo)
            
            else :
                
                j = 170
                
    if keyboard.is_pressed('w'):
            
            j = j - angleinc
            
            if j >= 10 :
                
                kit.servo[1].angle=j
                kit.servo[1].fraction = None

                time.sleep(tempo)
            
            else :
                
                j = 10
            
    print(i, j) 
            
