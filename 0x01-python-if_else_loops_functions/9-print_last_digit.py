#!/usr/bin/python3
def print_last_digit(number):
    digit = 0
    if number < 0:
        digit = -1 * number
        digit %= 10
        digit *= -1
    else:
        digit = number % 10
    print(digit, end="")
    return digit
