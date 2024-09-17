import RPi.GPIO as GPIO
import time

# Define GPIO pins for the stepper motor
control_pins = [7, 11, 13, 15]  # Adjust according to your wiring

# Set up the GPIO mode and pins
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)  # Set each pin as an output
    GPIO.output(pin, GPIO.LOW)  # Initialize each pin to LOW

# Define the step sequence for the 28BYJ-48 stepper motor
step_sequence = [
    [1, 0, 0, 0],  # Step 1: Energize coil 1
    [1, 1, 0, 0],  # Step 2: Energize coil 1 and 2
    [0, 1, 0, 0],  # Step 3: Energize coil 2
    [0, 1, 1, 0],  # Step 4: Energize coil 2 and 3
    [0, 0, 1, 0],  # Step 5: Energize coil 3
    [0, 0, 1, 1],  # Step 6: Energize coil 3 and 4
    [0, 0, 0, 1],  # Step 7: Energize coil 4
    [1, 0, 0, 1]   # Step 8: Energize coil 1 and 4
]

#this function is to rotate a specified number of steps 
#steps = number of positive for clockwise, negative for counterclockwise
#delay = delay between steps to control speed. 
def rotate_stepper(steps, delay):
    step_count = len(step_sequence)  # Number of steps in the sequence
    direction = 1 if steps > 0 else -1  # Determine direction of rotation (1 for clockwise, -1 for counterclockwise)
    
    # Loop through the specified number of steps
    for _ in range(abs(steps)):
        # Loop through each step in the sequence based on the direction
        for step in range(step_count)[::direction]:
            # Set GPIO pins according to the current step in the sequence
            for pin in range(4):
                GPIO.output(control_pins[pin], step_sequence[step][pin])
            time.sleep(delay)  # Wait for the specified delay between steps

def main():
    steps_moved = 0  # Track the total number of steps moved

    print("Press 'Ctrl+C' to stop the motor and return to the start position.")
    
    try:
        # Continuously rotate the motor until interrupted
        while True:
            rotate_stepper(1, 0.001)  # Rotate one step clockwise
            steps_moved += 1  # Increment the step counter

    except KeyboardInterrupt:
        # Handle the interrupt (Ctrl+C) to stop the motor and return to the start position
        print(f"Motor stopped after {steps_moved} steps.")
        
        time.sleep(1)  # Wait for a second before returning

        # Move back the same number of steps in the opposite direction (counterclockwise)
        print("Returning to the start position...")
        rotate_stepper(-steps_moved, 0.001)  # Rotate back by the same number of steps

    finally:
        # Clean up GPIO settings to ensure all pins are reset
        GPIO.cleanup()

# Run the main function when the script is executed
if __name__ == "__main__":
    main()

