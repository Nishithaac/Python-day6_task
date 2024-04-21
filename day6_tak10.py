"""
10) Given a list[4,2,-3,1,6] write a python program to find if there is a sub-list 
with sum equal to zero
"""




def subArray(arr, l):
    # Iterate through each index of the array except the last one
    for i in range(l - 1):
        # Initialize the sum with the current element
        s = arr[i]
        # Iterate through the remaining elements of the array
        for j in range(i + 1, l):
            # Add the current element to the sum
            s += arr[j]
            # Check if the sum equals zero
            if s == 0:
                # If the sum is zero, return True
                return True
    # If no subarray with sum zero is found, return False
    return False

# Given array
array = [4, 2, -3, 1, 6]

# Call the subArray function with the array and its length, and print the result
print(subArray(array, len(array)))
