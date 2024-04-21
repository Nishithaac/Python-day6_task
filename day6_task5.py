
"""
5) You have been given a list of N integers which represents the number of 
Mangoes in a bag.Each bag has a variable number of Mangoes. There are M
students in a Guvi class, your task is to distribute the Mangoes in such a way 
that each student  gets one bag. The difference between the number of Mangoes in a 
bag with maximum Mangoes and Bag with minimum Mangoes given to the
student is minimum?  


"""

# Function to calculate the binomial coefficient C(n, m)
def man(n, m):
    res = 1  # Initialising the result variable to 1

    # If m is greater than n - m, it's more efficient to compute C(n, m) as C(n, n - m)
    if m > n - m:
        m = n - m  # Set m to n - m to optimize calculation

    # Calculating the binomial coefficient using the formula C(n, m) = n! / (m! * (n - m)!)
    for i in range(0, m):
        res *= (n - i)  # Multiply res by (n - i)
        res /= (i + 1)  # Divide res by (i + 1)

    return res  # Return the calculated binomial coefficient

# Helper function for generating the number of ways to distribute n mangoes among m students
def calculate(n, m):
    # If there are not enough mangoes to distribute
    if n < m:
        return 0  # Return 0

    # Calculate the number of ways using the formula (m + n - 1)C(m - 1)
    ways = man(m + n - 1, m - 1)  # Calculate the binomial coefficient C(m + n - 1, m - 1)
    return int(ways)  # Return the integer value of ways

# Driver function
if __name__ == '__main__':
    # n represents the number of mangoes
    # m represents the number of people
    n = 7
    m = 5

    # Calculate the number of ways to distribute n mangoes among m students
    result = calculate(n, m)

    # Print the result
    print(result)