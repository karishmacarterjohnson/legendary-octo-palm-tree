'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''



def sumGame(list,k):
    for i in range(len(list)-1):
        for j in range(len(list)):
            if list[i] + list[j] == k:
                # if sum exists, print the match, return true, and stop
                print(f"{list[i]} + {list[j]} = {k}")
                return list[i] + list[j] ==k
                break
            elif (i== len(list)-2 and j == len(list)-1):
                print("no match")
                # if you hit the end of the array without a sum = k
            
'''
sample test cases: 
sumGame([10,5,6,3,7],17) --> 10 + 7 = 17
sumGame([1,4,6,20],100) --> no match

'''

#python sumGame.py
