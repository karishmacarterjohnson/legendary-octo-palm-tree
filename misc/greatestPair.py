'''
Given a list of numbers, return the greatest non-adjacent pair of numbers sum.

For example, given [10, 15, 3, 7], return 22 from 15 + 7
'''

def greatestPair(list):
    # number of combinations
    # combos =(((len(list)-2)*(len(list)-2+1))/2)
    
    # initalize pairs and array
    a, b = 0, 0
    sumPairs =[]
    for i in range(len(list)-2):
        for j in range(i+2,len(list)):
            # sum of non adjacent pair of numbers
            sum = list[i] + list[j]
            # TEST: print iterating sum pairs
            #print(f"{list[i]} + {list[j]} = {sum}")
            
            # append latest sum
            sumPairs.append(sum)
            
            # if the newest sum is the highest, update a and b, otherwise pass
            if sumPairs[len(sumPairs)-1] == max(sumPairs):
                a, b = list[i], list[j]
            else:
                pass
    print(f"greatest non-adjacent pair from {a} + {b} = {max(sumPairs)}")
    return sumPairs
  
# SAMPLE TESTS
# greatestPair([5, 1, 1, 5])