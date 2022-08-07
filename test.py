from comm.pwm import PWM
from time import sleep
import pyfirmata 


board = pyfirmata.Arduino("COM8")

driver1 = PWM(0x40)
driver2 = PWM(0x41)

driver1.setPWMFreq(60)
driver2.setPWMFreq(60)
while True:
    driver1.setPWM(0,125,250)
    sleep(1)
    driver1.setPWM(0,125,400)
    sleep(1)
    driver1.setPWM(0,125,600)
    sleep(1)