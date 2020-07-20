'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
'''

def lowestNonMatch(array):
    # initialize match variable that follows increments
    # starting with smallest element > 0 in array
    match = min(i for i in array if i > 0)
    for i in range(len(array)+1):
        # check for match using least nonnegative number
        if match in array:
            # increase match if correct thus far
            match +=1;

        else: 
            print(f"expected {match}")
            return match
            
# test function

# return 2
lowestNonMatch([3,4,-1,1])     

# return 3
lowestNonMatch([1,2,0])

# return 16
lowestNonMatch([-100,20,15])
