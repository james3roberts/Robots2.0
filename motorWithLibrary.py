#I know that this doesnt work but maybe I will find a library that will
import time
import keyboard  # For detecting keypress
from RPiStepper import RPiStepper

# Define GPIO pins for the stepper motor
control_pins = [7, 11, 13, 15]  # Adjust according to your wiring

# Initialize the stepper motor
stepper = RPiStepper(control_pins, mode="FULL")

steps_moved = 0  # Track the total number of steps moved

try:
    while not keyboard.is_pressed('s'):  # Press 's' to stop the motor
        stepper.set_speed(60)  # Set speed in RPM
        stepper.step(1)  # Rotate one step clockwise
        steps_moved += 1  # Increment the step counter

    print(f"Motor stopped after {steps_moved} steps.")

    time.sleep(1)  # Wait for 1 second before returning

    # Now move back the same number of steps in the opposite direction (counterclockwise)
    print("Returning to the start position...")
    stepper.set_speed(60)  # Set speed in RPM
    stepper.step(-steps_moved)  # Rotate back by the same number of steps

finally:
    # Cleanup GPIO when done
    stepper.cleanup()
