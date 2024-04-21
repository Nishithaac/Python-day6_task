"""
8)Write a python program to find the minimum element in a rated and sorted list 
"""


# Given list
mylist = [2, 5, 7, 1, 3, 4, 6]

# Printing  the unsorted list
print(f"Unsorted list: {mylist}")


# Iterating through each index of the list using range(len(mylist)-1)
for i in range(len(mylist)-1):
    # Iterating through each index of the list using range(len(mylist)-1)
    for j in range(len(mylist)-1):
        # Checks if the current element is greater than the next element
        if mylist[j] > mylist[j+1]:
            # If so, swap the elements
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

# Print the sorted list
print(f"Sorted list is: {mylist}")

# Print the minimum element in the sorted list
print(f"Minimum element in sorted list is: {mylist[0]}")
