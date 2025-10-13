number = int(input("Enter a number: "))
if number < 0:
    print("Natural numbers are not defined for negative numbers")
elif number == 0:
    print("0 is not a natural number")
else:
    print(number, "is a natural number")
# This program checks if a given number is a natural number.
# Example usage:
# Enter a number: 5
# 5 is a natural number
# Note: Natural numbers are positive integers starting from 1 (1, 2, 3, ...).