import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 16       #trigger pin
ECHO = 18       #echo pin

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

#converts a floating point into a 16th of an inch measurement
def inches_to_16th(inches):
    total_16th = int(inches * 16)
    whole_inches = total_16th // 16
    fraction_16th = total_16th % 16

#a basic dictionary to map specific 16th values
    fractions = {
        2: "1/8",
        4: "1/4",
        6: "3/8",
        8: "1/2",
        10: "5/8",
        12: "3/4",
        14: "7/8"
    }
    
    if fraction_16th in fractions:
        return f"{whole_inches} {fractions[fraction_16th]}" #check to see if the fractions dictionary needs to be used. 
    else:
        return f"{whole_inches}"        #returns the whole number
    
#start the loop of getting the measurements fo precision movements. 
try:
    while True:
        GPIO.output(TRIG, False)
        print('Waiting for sensor to settle...')
        time.sleep(0.5)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        pulse_start = time.time()
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        pulse_end = time.time()
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        # Calculate distance in centimeters
        distance_cm = (pulse_duration * 17150) / 2
        # Convert distance to inches and apply the blank offset of this sensor
        distance_inch = (distance_cm / 2.54) + 5.25
        # Convert to inches and fraction of 16th
        result = inches_to_16th(distance_inch)
        print(f"Measured distance: {result} inches")

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
