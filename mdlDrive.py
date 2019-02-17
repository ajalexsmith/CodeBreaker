######################################################################
# Holo chassis movement, to handle harmonic motion by PS3 Controlelr #
#         Speed based on position of controller             #
######################################################################
from approxeng.input.selectbinder import ControllerResource
import os
from time import sleep
import math
import ThunderBorg


TB1 = ThunderBorg.ThunderBorg()
TB1.i2cAddress = 11
TB1.Init()
TB2 = ThunderBorg.ThunderBorg()
TB2.i2cAddress = 10
TB2.Init()

def cls(): os.system('cls' if os.name == 'nt' else 'clear')


def motorSpeed(angle, speed):
    global TB1, TB2
    val = 0.0166666666667
    m1 = 0
    m2 = 0
    m3 = 0
    if angle >= -1 and angle < 60:
        dif = angle
        m1 = 1
        m2 = -1 + (dif * val)
        m3 = 0 - (dif * val)
    elif angle >= 60 and angle < 120:
        dif = angle - 60
        m1 = 1 #- (dif * val)
        m2 = 0 
        m3 = -1
    elif angle >= 120 and angle < 180:
        dif = angle - 120
        m1 = 0 - (dif * val)
        m2 = 1
        m3 = -1 + (dif * val)
    elif angle >= 180 and angle < 240:
        dif = angle - 180
        m1 = -1
        m2 = 1 - (dif * val)
        m3 = 0 + (dif * val)
    elif angle >= 240 and angle < 300:
        dif = angle - 240
        m1 = -1 + (dif * val)
        m2 = 0 - (dif * val)
        m3 = 1
    elif angle >= 300 and angle <= 360:
        dif = angle - 300
        m1 = 0 + (dif * val)
        m2 = -1
        m3 = 1 - (dif * val)

    print(str(m1))

    m1 = m1 * speed
    m2 = m2 * speed
    m3 = m3 * speed

    TB1.SetMotor1(m1)
    TB1.SetMotor2(m2)
    TB2.SetMotor1(m3)



def Drive(x, y):

    if abs(x) < 0.2 and abs(y) < 0.2:
        print(str(x) + " " + str(y))
        motorSpeed(0, 0)
    else:
        print(str(x) + " " + str(y))
        if x > 0.0 and y == 0.0:
            angle = 90
        elif x == 0.0 and y < 0.0:
            angle = 180
        elif x < -0.0 and y == 0.0:
            angle = 270
        elif x == 0.0 and y > 0.0:
            angle = 0
        else:
            angle = math.degrees(math.atan(abs(y) / abs(x)))
            angle = int(5 * round(float(angle) / 5))

            if x > 0.0 and y > 0.0:
                angle = 90 - angle
            elif x > 0.0 and y < 0.0:
                angle = 90 + angle
            elif x < 0.0 and y < 0.0:
                angle = 270 - angle
            elif x < 0.0 and y > 0.0:
                angle = 270 + angle

        speed = min(math.sqrt((x * x) + (y * y)), 1)

        if speed < 0.2:
            speed = 0
        print(str(angle))
        #print(str(speed))

        motorSpeed(angle, speed)





def StartMotion():

    while True:
        try:
            with ControllerResource() as joystick:
                print('Found a joystick and connected')
                while joystick.connected:
                    Drive(round(joystick.rx, 2), round(joystick.ry, 2))
            # Joystick disconnected...
            print('Connection to joystick lost')
        except IOError:
            # No joystick found, wait for a bit before trying again
            print('Unable to find any joysticks')
            sleep(1.0)
