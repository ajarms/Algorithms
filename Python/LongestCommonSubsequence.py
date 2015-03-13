'''
dynamic lcs algorithm
'''
import random



def random_string (n):
    rand_string = ''
    alph = 'aaabcdeeefghiiijklmnooopqrstuuuvwxyz'

    for i in range(0,n):
        k = random.randrange(0,len(alph))
        rand_string += alph[k]
    
    return rand_string



def lcs(a, b):

    # switch to print additional information
    p_all = False
    
    # create a table
    m,n = len(a), len(b)
    c = [[0 for x in range(m+1)]for y in range(n+1)]

    # fill the table
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1] == b[j-1]:
                c[j][i] = c[j-1][i-1] + 1
            elif c[j][i-1] >= c[j-1][i]:
                c[j][i] = c[j][i-1]
            else:
                c[j][i] = c[j-1][i]

    # optional printout of table
    if p_all == True:
        for i in range(n+1):
            print(c[i])    

    # use the table to rebuild an LCS string
    # optional print of table traversal
    sub = ''
    while c[n][m] != 0:
        if c[n][m]==c[n-1][m]:
            if p_all == True:
                print(c[n][m], '\t↑')
            n -= 1
        elif c[n][m-1]==c[n][m] and c[n-1][m-1]==c[n-1][m]:
            if p_all == True:
                print(c[n][m], '\t←')
            m -= 1
        else:
            sub = a[m-1]+sub
            if p_all == True:
                print(c[n][m],'\t↖\t'+sub)
            m -= 1
            n -= 1
    
    return sub



x,y = random_string(random.randrange(6,16)), random_string(random.randrange(6,16))
z = lcs(x,y)
print (x, '&', y, '\nLCS Length is:\t', len(z), '\nOne LCS is:\t '+ z)
