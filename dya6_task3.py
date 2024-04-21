"""
3) Given a Python List [10,501,22,37,100,999,87,351] Find out how many numbers are 
there in the given Python List which are happy numbers 
"""
# Given list of numbers
a = [10, 501, 22, 37, 100, 999, 87, 351]

# Initialize an empty list to store happy numbers
b = []

# Defining  a function named 'happy' that takes a list 'a' as input
def happy(a):
    # Iterating through each number in the list 'a'
    for i in range(len(a)):
        sum = a[i]  # Get the current number
        
        # Continuing  the loop until 'sum' becomes 1 (happy number) or 4 (unhappy number)
        while sum != 1 and sum != 4:
            
            # Initialising  a temporary variable to store the sum of squares of digits
            tempsum = 0
            
            # Iterating  through each digit of the number
            for digit in str(sum):
                
                # Calculating  the sum of squares of digits and add it to tempsum
                tempsum += int(digit) ** 2
            
            # Updating  'sum' with the new calculated sum
            sum = tempsum
            
        # If 'sum' is 1, the current number is a happy number
        if sum == 1:
            # Appending  the happy number to the list 'b'
            b.append(a[i])
    
    # Returning  the list of happy numbers
    return b

# Printing  the list of happy numbers returned by the 'happy' function
print(f"The happy numbers from list {a} are:",happy(a))


