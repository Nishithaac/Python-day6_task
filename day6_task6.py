
"""
6) You have been given three lists. Your task is to find the dupliates in three 
lists. Write a python program for the same. You can use your own python lists?

"""
#method1
# Given three lists
list1=[1,5,10,20,80,50]
list2=[6,7,20,80,100]
list3=[3,4,15,20,30,50,70,80]

# Initialising  an empty list to store common elements
common=[]

# Iterating through each element in list1
for i in list1:
    # Iterating through each element in list2
    for j in list2:
        # Iterating through each element in list3
        for k in list3:

            # Checks if the current element is common in all three lists
            if i==j==k:
                # If the element is common, append it to the common list
                common.append(i)
# Print the duplicates found in the three lists
print(f" Duplicates in three lists {list1},{list2},{list3} are: {common}")

#method2

#Given three lists
list1=[1,5,10,20,80,50]
list2=[6,7,20,80,100]
list3=[3,4,15,20,30,50,70,80]

# Initialising an empty list to store common elements
result=[]

# Iterating through each element in list1
for i in list1:

     # Checks if the current element is present in both list2 and list3
    if i  in list2 and i in list3:

        
        # If the element is present in both lists, append it to the result list
        result.append(i)


# Print the duplicates found in the three lists
print(f" Duplicates in three lists {list1},{list2},{list3} are: {result}")