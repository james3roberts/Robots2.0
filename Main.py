import Measuring
import Stepper

def get_number():
    cut_number = float(input('Enter a number less than 22.25: '))
    while cut_number >= 22.25:
        print("number must be less than 22.25")
        cut_number = float(input('Enter a number less than 22.25: '))
    return cut_number

