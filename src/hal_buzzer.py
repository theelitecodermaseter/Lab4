import time
import RPi.GPIO as GPIO #import RPi.GPIO module


def init():
    from time import sleep  # used to create delays0.5
    GPIO.setmode(GPIO.BCM)  # choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(18, GPIO.OUT)  # set GPIO 18 as output


def deinit():
    PWM = GPIO.PWM(18, 0)

    PWM.stop()
    GPIO.cleanup()



def short_beep(beep_interval):

    #Set PWM frequency to 100Hz
    PWM = GPIO.PWM(18, 5000)

    #Set PWM to 50% Duty Cycle and start PWM
    PWM.start(50)

    #delay for 100ms
    time.sleep(beep_interval)

    #Stop buzzer
    PWM.stop()

    #Delay for 100ms
    time.sleep(beep_interval)

    #Start PWM at 50% Duty Cycle
    PWM.start(50)

    #Delay for 100ms
    time.sleep(beep_interval)

    #Stop Buzzer
    PWM.stop()


