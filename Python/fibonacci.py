number = int(input("Enter a number: "))
if n <= 0:
    print("Fibonacci sequence is not defined for non-positive integers")
else:
    a, b = 0, 1
    print("Fibonacci sequence up to", number, ":")
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
# This program prints the Fibonacci sequence up to a given positive integer.
# Example usage:
# Enter a number: 7
# Fibonacci sequence up to 7 :
# 0 1 1 2 3 5 8
# Note: Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.