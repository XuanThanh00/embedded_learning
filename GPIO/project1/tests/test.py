from drivers.GPIO import GPIO
from time import sleep_ms

LED = GPIO(15)
LED.enable_gpio_out()

button = GPIO(18)
button.clear_oe_bit()


while True:
    
    button_state = button.read_gpio()
    if button_state == 1:
        print("true")
        LED.set_gpio()
    else:
        print("false")
        LED.reset_gpio()
    sleep_ms(100)
