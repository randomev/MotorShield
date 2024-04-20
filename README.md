# Motor-Shield

The Motorshield is designed to help you get your Raspberry Pi-based Robot. This board can control the DC motor as well as the stepper motor. You can connect your IR and Ultrasonic sensors to tell your robot about its environment. You can easily make your Line Following, Object following, Wall following, and Maze-Solver Robots.
Motor Driver for Raspberry Pi to control DC and Stepper Motors

<img src="https://cdn.shopify.com/s/files/1/1217/2104/products/3_1_481fe438-49c9-45f4-805c-ea60c02055d2_700x.png?v=1611396591" width="300">


**Steps for Motor Shield software installation -** 

1. Open Terminal and download the code by writing: 
   ```
   git clone https://github.com/randomev/MotorShield.git
   ```

2. Your code will be downloaded to '/home/pi' directory. Use 'ls' command to check the list of directories.

3.  Go to directory 'MotorShield' and open 'Test_Motor.py'

4. Run (Press F5) file 'Test_Motor.py'. This is the example code to run all the motors in 'Forward' and 'Backward' direction

5. For interfacing Stepper Motor use example code 'Stepper_Test.py'

6. In Raspberry 5, you need to do

sudo apt remove python3-rpi.gpio
sudo apt install python3-rpi-lgpio

https://rpi-lgpio.readthedocs.io/en/latest/install.html

https://forums.raspberrypi.com/viewtopic.php?p=2160578#p2160578

Motor 4 pin 32 collides, seen with this:
gpioinfo 4|grep "\[used"

So motor4 is can't be used for now with pi 5?

https://rpi-lgpio.readthedocs.io/_/downloads/en/latest/pdf/


## Motorshield GUI
![PiRelay GUI](https://github.com/sbcshop/MotorShield/blob/master/Images/PiRelay_GUI.png)

**Changes:**

Added __Motor__, __LinkedMotor__, __Arrow__ and __Sensor__ classes. Allows user to specify what is "forward" and what is "reverse" without requiring re-wiring of the motors.
