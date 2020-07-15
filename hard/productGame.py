'''
Given an array of integers, return a new array such that each element at index i 
of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''

def productGame(list):
    # initialize output vector
    products = [0 for x in range(len(list))]
    # iterate through each item in input list
    for i in range(len(list)):
        # initialize prod as 1
        prod = 1
        # loop through all the terms in list
        for j in range(len(list)):
            # when its anything but the specified term, multiply
            if(j!=i):
                prod*= list[j]
        # update product vector        
        products[i] = prod
    print(f"all others multiplied:{products}")
    return products     

# test function
productGame([1,2,3,4])
