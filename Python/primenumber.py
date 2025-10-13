number = int(input("Enter a number: "))
if number > 1:
    for i in range(2, int(number**0.5) + 1):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")
# This program checks if a given number is a prime number or not.
# Example usage:
# Enter a number: 29
# 29 is a prime number
