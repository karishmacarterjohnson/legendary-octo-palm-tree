'''
Given an array of integers, find the first missing integer in linear time and constant space. 
In other words, find the lowest integer that does not exist in the array.
'''



def failIncrement(array):
    # initialize match variable that follows increments
    # starting with first element in array
    match = array[0];
    for i in range(len(array)):
        # loop though array length times testing if value is as predicted
        if(match == array[i]):
            # increase match if correct thus far
            match+=1;
        else: 
            return match
            
# test function

# expects 3,4,5, return 5
failIncrement([3,4,-1,1])     

# expects 1,2,3, return 3
failIncrement([1,2,0])
