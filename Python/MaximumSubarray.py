import random

'''
implement a maximum subarray algorithm
'''

def make_random ():

    rand_list = []

    for i in range(0,100):
        rand_list.append(random.randrange(-50,50))
    
    return rand_list


def max_sub(numlist):
    
    max_sum_ending_here = max_sum = numlist[0]

    for i in range(1, len(numlist)):
        max_sum_ending_here = max(numlist[i], max_sum_ending_here + numlist[i])

        if max_sum_ending_here == numlist[i]:
            startind = i
        
        max_sum = max(max_sum, max_sum_ending_here)

        if max_sum == max_sum_ending_here:
            endind = i 


    return numlist[startind:endind]


test = make_random()
print (test,'\n')
print(max_sub(test))

