import time
from RPiStepper import RPiStepper   #import could not be resolved.


# Define GPIO pins for the stepper motor
control_pins = [7, 11, 13, 15]  # wiring based on how I wired the motor to the board. 

# Initialize the stepper motor
stepper = RPiStepper(control_pins, mode="FULL")  # or "HALF" for half-stepping

# Function to rotate the stepper motor
def rotate_stepper(steps, speed):
    """
    Rotates the stepper motor by a specified number of steps.
    
    :param steps: Number of steps to rotate (positive for clockwise, negative for counterclockwise)
    :param speed: Speed of rotation in RPM
    """
    stepper.set_speed(speed)  # Set the speed of the motor
    stepper.step(steps)  # Rotate the motor by the specified number of steps

try:
    # Rotate 32 steps (one full revolution for 28BYJ-48 motor) clockwise at 60 RPM
    rotate_stepper(32, 60)

    time.sleep(1)  # Wait for a second

    # Rotate 16 steps counterclockwise at 30 RPM
    rotate_stepper(-16, 30)

finally:
    # Cleanup GPIO when done
    stepper.cleanup()
