import socket

import hal_lcd
from time import sleep

import hal_buzzer


def main():
    #Instantiate and initialize the LCD driver
    lcd = hal_lcd.lcd()

    sleep(0.5)
    lcd.backlight(0)  # turn backlight off

    sleep(0.5)
    lcd.backlight(1)  # turn backlight on

    lcd.lcd_clear()
    lcd.lcd_display_string("Hi welcome to", 1)  # write on line 1
    lcd.lcd_display_string("DevOps for AIoT", 2)  # write on line 2
    # starting on 3rd column

    sleep(2)  # wait 2 sec

    #Get IP address
    local_ip_address = socket.gethostbyname("raspberrypi")

    #Display current Raspbery Pi IP Address
    lcd.lcd_clear()
    lcd.lcd_display_string("IP Address: ", 1)
    lcd.lcd_display_string(local_ip_address, 2)


    #Buzzer beep
    hal_buzzer.hal_buz_init()
    hal_buzzer.hal_buz_short_beep(0.1)


#Main entry point
if __name__ == "__main__":
    main()

