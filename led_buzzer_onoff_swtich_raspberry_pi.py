import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setup(21,gpio.OUT)
gpio.setup(20,gpio.OUT)
gpio.setwarnings(False)
try:
    while (True):
        for j in  range(5,1,-1):
            for i in range(0,2):
                gpio.output(21,True)
                gpio.output(20,False)
                print"LED ON   BUZZER OFF"

                time.sleep(j/10.0)
                gpio.output(21,False)
                gpio.output(20,True)
                print"LED OFF   BUZZER ON"
                time.sleep(j/10.0)


except:
    gpio.cleanup()
    print "Error in Execution"