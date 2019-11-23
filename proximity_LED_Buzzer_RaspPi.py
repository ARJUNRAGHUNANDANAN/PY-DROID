import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
trigger=23
echo=24
buzzer=25
gp.setup(trigger,gp.OUT)
gp.setup(buzzer,gp.OUT)
gp.setup(echo,gp.IN)
gp.output(trigger,False)
print "waiting for the sensor to settle"
time.sleep(2)

while(True):
    gp.output(trigger,True)
    time.sleep(0.00001)
    gp.output(trigger,False)
    while gp.input(echo)==0:
        pulse_start =time.time()
    while gp.input(trigger)==1:
        pulse_end =time.time()
    pulse_duration=pulse_end-pulse_start
    distance = pulse_duration*17150
    distance =round(distance,2)
    print "Distance :",distance,"cm"
    if (distance<=15):
        gp.output(buzzer,True)
    else:
        gp.output(buzzer,False)
