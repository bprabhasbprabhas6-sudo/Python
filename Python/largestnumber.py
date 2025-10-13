first_number = int(input("enter first number:"))
second_number = int(input("enter second number:"))
third_number = int(input("enter third number:"))
if largest_number >= second_number and largest_number >= third_number:
    print("The largest number is:", first_number)
elif second_number >= first_number and second_number >= third_number:
    print("The largest number is:", second_number)
else:
    print("The largest number is:", third_number)
largest_number = first_number
# This program finds the largest of three numbers provided by the user.
# Example usage:
# enter first number:10
# enter second number:20
# enter third number:15
# The largest number is: 20
# Note: The program assumes that the user inputs valid integers.