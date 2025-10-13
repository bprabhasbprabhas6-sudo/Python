number = int(input("Enter a number: "))
if  number < 0:
    print("Armstrong numbers are not defined for negative numbers")
else:
    sum_of_cubes = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum_of_cubes += digit ** 3
        temp //= 10
    if number == sum_of_cubes:
        print(number, "is an Armstrong number")
    else:
        print(number, "is not an Armstrong number")
# This program checks if a given number is an Armstrong number or not.
# Example usage:
# Enter a number: 153
# 153 is an Armstrong number
# Note: Armstrong numbers are typically defined for non-negative integers.
