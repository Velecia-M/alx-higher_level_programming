#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
last_digit = -(number)
strx = "Last digit of {} is {}".format(number, last_digit)
if last_digit > 5:
    print(f"{strx} and is greater than 5")
elif last_digit == 0:
    print(f"{strx} and is 0")
else:
    print(f"{strx} and is less than 6 and not 0")
