import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BOARD)

TRIG = 16
ECHO = 18

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

#this does not seem to be doing the conversions so it will need to be changed
def inches_to_16th(inches):
    total_16th = int(inches *16)
    whole_inches = total_16th//16
    fraction_16th = total_16th%16
    return whole_inches, fraction_16th

try:
    while True:
        GPIO.output(TRIG,False)
        print('Waiting For Sensor to Settle')
        time.sleep(.5)

        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        pulse_start=time.time()
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()

        pulse_end = time.time()
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end- pulse_start 

        distance = (pulse_duration*17150/2)
        #test distance = 16.5 inches.
        distance_inch=distance /2.54 + 5.25  #this is to get the sensor set to zero
        whole_inches, fraction_16th = inches_to_16th(distance_inch)
        print(f'distance: {whole_inches} {fraction_16th}/16 inches')

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()


#for some reason this is measuring at 22 13/16 when it should be about 18 inches
