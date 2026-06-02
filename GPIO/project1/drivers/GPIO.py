from config.config import *
from machine import mem32
from time import sleep_ms

class GPIO:
    def __init__(self, pin):
        self.pin = pin
        
    def bit_shifting(self):
        if self.pin < 32:
            return (1 << self.pin)
        else:
            return (1 << (self.pin - 32))

    def enable_gpio_out(self):
        if self.pin < 32:
            mem32[GPIO_ENABLE_REG] |= self.bit_shifting()
        else:
            mem32[GPIO_ENABLE1_REG] |= self.bit_shifting()

    def set_gpio(self):
        if self.pin < 32:
            mem32[GPIO_OUT_W1TS_REG] |= self.bit_shifting()
        else:
            mem32[GPIO_OUT1_W1TS_REG] |= self.bit_shifting()

    def reset_gpio(self):
        if self.pin < 32:
            mem32[GPIO_OUT_W1TC_REG] |= self.bit_shifting()
        else:
            mem32[GPIO_OUT1_W1TC_REG] |= self.bit_shifting()
    
    def toggle_gpio(self):
        if self.pin < 32:
            pin_state = (mem32[GPIO_OUT_REG] >> self.pin) & 1
            
        else:
            pin_state = (mem32[GPIO_OUT1_REG] >> (self.pin - 32)) & 1
            
        if current_state == 1:
            self.reset_gpio() 
        else:
            self.set_gpio()
    
    def clear_oe_bit(self):
        mask = self.bit_shifting() ^ 0xFFFFFFFF
        if self.pin < 32:
            mem32[GPIO_ENABLE_REG] &= mask
        else:
            mem32[GPIO_ENABLE1_REG] &= mask
            
    def read_gpio(self):
        if self.pin < 32:
            return (mem32[GPIO_IN_REG] >> self.pin) & 1
        else:
            return (mem32[GPIO_IN1_REG] >> (self.pin - 32)) & 1
        
