"""
4) Write a python program to find the sum of first and last digit of an integer?
"""
# Given number
num=123

# Converting the number to a string to access individual digits
num=str(num)

# Getting  the first digit of the number by accessing the character at index 0 and convert it back to an integer
firstDigit=int(num[0])

 # Getting  the last digit of the number by accessing the character at index -1 (last position) and convert it back to an integer
lastDigit=int(num[-1])

# Calculating the sum of the first and last digits
addition=firstDigit+lastDigit

# Printing the sum of the first and last digits along with their values
print(f"Sum of first digit:{firstDigit} and last digit:{lastDigit} is: {addition}")
