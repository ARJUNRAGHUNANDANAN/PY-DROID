import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TRIG=23
ECHO=24
BUZZ=25
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(BUZZ,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG,False)
print "waiting for the sensor to settle"
time.sleep(2)

while(True):
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulse_start =time.time()
    while GPIO.input(ECHO)==1:
        pulse_end =time.time()
    pulse_duration=pulse_end-pulse_start
    distance = pulse_duration*17150
    distance =round(distance,2)
    print "Distance :",distance,"cm"
    if (distance<=15):
        GPIO.output(BUZZ,True)
    else:
        GPIO.output(BUZZ,False)