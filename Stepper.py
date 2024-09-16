import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

control_pins = [7,11,13,15]

for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

halfstep_seq = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
]

#original_position = 0 #this is the starting position
try:
    while True:
        for halfstep in range(8):
            for pin in range (4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)
        #original_position = 0 #this saves the final position
except KeyboardInterrupt:
    pass
finally:
    #move back to the start
    # for _ in range(original_position, 0,-1):
    #     for halfstep in range(8,-1,-1):
    #         for pin in range(4):
    #             GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
    #         time.sleep(0.001)
    GPIO.cleanup() 