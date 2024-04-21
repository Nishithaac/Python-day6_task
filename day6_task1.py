"""
1)You have been given a python List[10,501,22,37,100,999,87,351] your task is to 
create two lis one which have all the Even numbers and another List which have 
all the ODD numbers in it?

"""
# Given list
mylist=[10,501,22,37,100,999,87]

# Initialising  two empty lists to store even and odd numbers
list1=[]
list2=[]

# Iterate\ing  through each element in the given list
for i in mylist:

    # This condition checks if the current element is even
    if i%2==0:
        # If the element is even, append it to list1
        list1.append(i)

    else:
        # If the element is odd, append it to list2
        list2.append(i)
# Printing  the list of even numbers
print(f"Even numbers are: {list1}")

# Printing  the list of odd numbers
print(f"ODD numbers are: {list2}")

