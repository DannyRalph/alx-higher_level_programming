#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

print("Last digit of {} is {} and is".format(number, last_digit), end="")

if last_digit > 5:
    print(" greater than 5".format(number, last_digit))
elif last_digit == 0:
    print(" 0".format(number, last_digit))
else:
    print(" less than 6 and not 0".format(number, last_digit))
