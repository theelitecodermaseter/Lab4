# System imports
import socket
import time
from time import sleep


# Local imports

#from ..hal import hal_dc_motor as dc_motor


from src.hal import  hal_lcd as LCD



def blink_led():
    # Led Blink
    led.init()

    led.set_output(0, 1)
    time.sleep(0.5)

    led.set_output(0, 0)
    time.sleep(0.5)

    led.set_output(0, 1)
    time.sleep(0.5)

    led.set_output(0, 0)
    time.sleep(0.5)


def rotate_servo():
    servo.init()

    for i in range(0, 180, 5):
        servo.set_servo_position(i)
        sleep(0.05)


def test_motor():
    dc_motor.init()
    dc_motor.set_motor_speed(100)

    sleep(2)


def main():
    # Instantiate and initialize the LCD driver
    lcd = LCD.lcd()

    sleep(0.5)
    LCD.backlight(0)  # turn backlight off

    sleep(0.5)
    LCD.backlight(1)  # turn backlight on

    LCD.lcd_clear()
    LCD.lcd_display_string("Hi welcome to", 1)  # write on line 1
    LCD.lcd_display_string("DevOps for AIoT", 2)  # write on line 2
    # starting on 3rd column

    sleep(2)  # wait 2 sec

    # Get IP address
    local_ip_address = socket.gethostbyname("raspberrypi")

    # Display current Raspbery Pi IP Address
    LCD.lcd_clear()
    LCD.lcd_display_string("IP Address: ", 1)
    LCD.lcd_display_string(local_ip_address, 2)

    # Buzzer beep
    buzzer.init()
    buzzer.short_beep(0.1)

    blink_led()

    rotate_servo()

    test_motor()


# Main entry point
if __name__ == "__main__":
    main()
