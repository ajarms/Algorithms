import random
import time

'''
implement an optimized quicksort that uses insertion sort to close the deal
'''

def make_random ():
    rand_list = []
    for i in range(0,100):
        rand_list.append(random.randrange(0,100))
    
    return rand_list

def insertion(A):
    for i in range(1,len(A)):
        for n in range(i,0,-1):
            if A[n] < A[n-1]:
                A[n], A[n-1] = A[n-1], A[n]
            else:
                break


def quick(A, l, r, k):    
    # pick a good maximum insertion sort size
    # normally, if not passed off to insertion sort, k = 2
        

    if r-l > k:
        # pick pivot, approx median approach to optimize
        p = get_pivot(A, l, r)
        
        pivot = A[p]

        #print(A,"\n")

        #print('pivot key = ',p,'\tval = ',pivot,'\n')
        
        A[r], A[p] = A[p], A[r] # get pivot out of the way
        s = l
        #s2 = r-1    # needed for optimization to detect numbers == pivot
        for i in range(l,r):  # doesn't check item r, which holds pivot
            if A[i] < pivot:
                A[i], A[s] = A[s], A[i] # same issue, i == s ??
                s += 1
            '''
            if A[i] > pivot:
                A[i], A[s2] = A[s2], A[i]
                s2 -= 1
                '''
        A[s], A[r] = A[r], A[s] # put pivot in it's new place

        #print(A,"\n\n")
        
        quick(A, l, s-1, k)
        quick(A, s+1, r, k)


def optimized_quick(A, l, r, k):
    quick(A, l, r, k)
    insertion(A)

# theoretically more efficient
# the ideal pivot is the true median of the set
# this takes the median of the first, middle, and last items
def get_pivot(A, l, r):
    m = r//2

    if A[l] >= A[m] >= A[r] or A[r] >= A[m] >= A[l]:
        p = m
    elif A[m] >= A[r] >= A[l] or A[l] >= A[r] >= A[m]:
        p = r
    else:
        p = l

    return p

# this section is to test the sorting efficiency for different values of k
# turns out, on my laptop for this algorithm, 8<=k<=10 is the ideal range
'''
avgruns = []
timesum = 0

for i in range(2,20):
    timesum = 0
    for n in range(1000):
        test = make_random()
        start = time.clock()
        optimized_quick(test, 0, len(test)-1, i)
        end = time.clock()
        timesum += end - start
    timeavg = timesum/1000
    avgruns.append(timeavg)

for i in range(0,len(avgruns)):
    print(i+2,":\t", avgruns[i])
'''

test = make_random()
print (test)
optimized_quick(test, 0, len(test)-1, 9)
print (test)
