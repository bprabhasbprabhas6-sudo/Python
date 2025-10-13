number = int(input("enter a number:"))
factorial = 1
if number < 0:
    print("Factorial is not defined for negative numbers")
elif number == 0 or number == 1:
    print("Factorial of", number, "is 1")
else:
    for i in range(2, number + 1):
        factorial *= i
    print("Factorial of", number, "is", factorial)
# This program calculates the factorial of a given non-negative integer.
# Example usage:
# enter a number:5
# Factorial of 5 is 120
# Note: Factorial of negative numbers is not defined.