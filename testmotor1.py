#!/usr/bin/python

import PiMotor
import time
import RPi.GPIO as GPIO

#Name of Individual MOTORS 
m1 = PiMotor.Motor("MOTOR1",1)


try:
    while True:
        for speed in range(15,100):
                print("F {}".format(speed))
                m1.forward(speed)
                time.sleep(2)
                print("B ")
                m1.reverse(speed)
                time.sleep(2)
        
except KeyboardInterrupt:
    GPIO.cleanup()

    
