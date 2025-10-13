string = input("Enter a string: ")
reversed_string = string[::-1]
if string == reversed_string:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
# This program checks if a given string is a palindrome.
# Example usage:
# Enter a string: racecar
# racecar is a palindrome