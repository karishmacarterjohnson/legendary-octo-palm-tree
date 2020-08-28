''' 
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).

rand5() randomly outputs int from 1 to 5
rand7() uses rand5s output to produce random value between 1 and 7 by randomly adding or substracting values
'''

import random 

def rand5():
    return random.randint(1,5)
    
def rand7(rand5):
    # randomize addition or subtraction from rand5 output
    pm = random.randint(1,2)
    # if 1: add random value from 0 to where max value = 7
    if pm == 1:
        return rand5 + random.randint(0,7-rand5)
    # otherwise (i.e. pm = 2) subtract random int from
    # 0 to where min value = 1
    else:
        return rand5 - random.randint(0, rand5-1)
    

x = rand5()
print(x)
print(rand7(x))