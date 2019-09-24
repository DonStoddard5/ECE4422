#! /usr/bin/python

from gpiozero import Servo
from time import sleep

servoPIN = 17 #this must be the GPIO# not the physical pin #. e.g. to use pin 11 (GPIO17), this must be 17 
print ("servomotor.py exicuted")

moveDelay=0.75

myCorrection=0.2
maxPW=(2.0+myCorrection)/1000
minPW=(1.0-myCorrection-.1)/1000
 
servo = Servo(servoPIN,min_pulse_width=minPW,max_pulse_width=maxPW)
servo.value=-1
sleep(moveDelay)
servo.value=1
sleep(moveDelay)
servo.value=0
sleep(moveDelay)

while True:
    servoPos = input("Enter positioin value between -1 and 1: ")
    servoPos = float(servoPos)
    if servoPos <= 1 and servoPos >= -1:
        servo.value=servoPos
    else:
        print("ERROR: Position value must be between -1 and 1.")

servo.stop()
GPIO.cleanup();

