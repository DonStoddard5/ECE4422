To install this package, first download the files to your desired directory. Then in terminal, navigate to that directory and run this command:
```
sudo pip3 install -e .
```
This will install the package and you're ready to go. 

The example script is named
```
./ServoMotor2/servomotor2.py
```
It will allow you to control a servo motor using values between -1 and 1. Connect the ground wire of the servo to a ground pin, the Vcc wire to 3.3 volts, and the control wire to pin 11, which is the same as GPIO17.
