#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 1
if number < 0:
    sign = -1
lst = ((number * sign) % 10) * sign
if lst > 5:
    print(f"Last digit of {number} is {lst} and is greater than 5");
elif lst == 0:
    print(f"Last digit of {number} is {lst} and is 0");
else:
    print(f"Last digit of {number} is {lst} and is less than 6 and not 0");
