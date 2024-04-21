
"""
7) Write a python program to find the first non-repeating elements in a given list of
integers?

"""
# Given list
mylist = [10, 30, 40, 20, 10, 20, 50, 10]

# Initialising an empty list to store non-repeating elements
non_repeating = []

# Iterating  through each element in the list
for i in mylist:
    # Checks the count of occurrences of the current element in the list
    if mylist.count(i) == 1:
        # If the count is 1, it means the element is non-repeating, so append it to the non_repeating list
        non_repeating.append(i)

# Print the list of non-repeating elements
print(non_repeating)

# Print the first non-repeating element
print(f"The first non-repeating element is {non_repeating[0]}")


# method2:
# Given list
mylist = [10, 30, 40, 20, 10, 20, 50, 10]

# Initialising an empty list to store non-repeating elements
non_repeating = []

# Iterating through each index of the list using range(len(mylist))
for i in range(len(mylist)):
    # Checks if the current element at index i is not present before or after index i
    if mylist[i] not in mylist[0:i] and mylist[i] not in mylist[i+1:]:
        # If the element is not repeated, append it to the non_repeating list
        non_repeating.append(mylist[i])

# Print the list of non-repeating elements
print(non_repeating)

# Print the first non-repeating element
print(f"The first non-repeating element is {non_repeating[0]}")