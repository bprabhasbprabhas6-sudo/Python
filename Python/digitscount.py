number = int(input("Enter a number: "))
count = 0
if number < 0:
    print("Digit count is not defined for negative numbers")
elif number == 0:
    count = 1
    print("Number of digits in", number, "is", count)
else:
    temp = number
    while temp > 0:
        temp //= 10
        count += 1
    print("Number of digits in", number, "is", count)
# This program counts the number of digits in a given non-negative integer.
# Example usage:
# Enter a number: 12345
# Number of digits in 12345 is 5
# Note: Digit count for negative numbers is not defined.