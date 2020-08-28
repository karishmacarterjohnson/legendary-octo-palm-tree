'''
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
'''

def maxsubarrays(arr,k):
    # initialize array for max in subset arrays
    maxinarr = []
    # iterate to create all subset arrays of k length
    # store max of each subset array in maxinarr 
    for i in range(0,len(arr)-k+1):
        maxinarr.append(max(arr[i:i+k]))
    # return all max values from each subset array
    return maxinarr

print(maxsubarrays([10,5,2,7,8,7],3))