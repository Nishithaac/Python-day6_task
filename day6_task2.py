"""
2) Given a Python List [10,501,22,37,100,999,87,351] your task is to Count all the
Prime Nubers and create a new Python List which will contain all the Prime Numbers
in it?
"""
# Given list
mylist=[10,501,22,37,100,999,87]

# Initialising an empty list to store prime numbers
list1=[]


# Iterating through each element in the given list
for i in mylist:
    # Initialising a counter to count the number of factors of the current element
    count=0

    # Iterating  from 1 to (i - 1)
    for j in range(1,i):
        # Checks if j is a factor of i
        if i%j==0:
            # If j is a factor, increment the counter
            count=count+1
     # Check if the counter is equal to 1 (meaning only 1 and i are factors)
    if count==1:
        # If the counter is 1, it means i is a prime number, so append it to list1
        list1.append(i)

#printing the count of prime numbers
print("The count of prime numbers is:",len(list1))
# Print the list of prime numbers
print(f" The prime numbers are: {list1}")

