"""
9) You have been given a Python list [10,20,30,9] and a value of 59.Write a python
progrm to find triplet in the list whose sum is equal to the given value
"""



# Given list of integers
mylist = [10, 20, 30, 9]

# Given value to find triplets
value = 59

# Checks if the sum of the first three elements equals the given value
if mylist[0] + mylist[1] + mylist[2] == value:
    # If so, print the triplet
    print(f"The triplet of {value} is: {mylist[0], mylist[1], mylist[2]} ")

# Checks if the sum of the second, third, and fourth elements equals the given value
elif mylist[1] + mylist[2] + mylist[3] == value:
    # If so, print the triplet
    print(f"The triplet of {value} is: {mylist[1], mylist[2], mylist[3]} ")


#method 2
# Import the combinations function from itertools module
from itertools import combinations

# Define a function to find triplets in the list that sum up to the given key
def findTriplets(lst, key):
    # Define a function to check if the sum of elements in a combination equals the key
    def valid(val):
        return sum(val) == key
    
    # Generate all combinations of 3 elements from the list
    # Filter out only those combinations where the sum equals the key
    # Convert the filtered combinations to a list and return it
    return list(filter(valid, list(combinations(lst, 3))))

# Given list
lst = [10, 20, 30, 9]

# Call the findTriplets function with the given list and key
print(findTriplets(lst, 59))
