'''
Matrix-Chain Multiplication
'''


# provided input, matching textbook example
m_in = '30 35\n35 15\n15 5\n5 10\n10 20\n20 25'


# extracts data in format for MCM
def extract(s):
    s1 = s.split()
    out = [s1[0]]
    for i in range(1,len(s1),2):
        out.append(s1[i])
    out = [int(o) for o in out]
    return out
        

# matrix-chain order algorithm
def mcm(p):
    n = len(p)-1
    m = [[0 for i in range(n)]for j in range(n)]
    s = [[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        m[i][i] = 0
    # for l=2 to n
    for l in range(2,n+1):
        # for i=1 to n-l+1** modified, i & j refer to indexes
        for i in range(n-l+1):
            j = i+l-1
            m[i][j] = float('inf')
            # for k=i to j-1
            for k in range(i,j):
                q = m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    #return (m,s)
    return (m[0][n-1])


# print both tables output by mcm
def mcm_print(t):
    m,s = t
    for row in m:
        print(row)
    print('\n')
    for row in s:
        print(row)


# print optimal parenthesization
def optimal_print(s,i,j):
    if i==j:
        print ('A'+str(i+1),end='')
    else:
        print('(',end='')
        optimal_print(s,i,s[i][j])
        optimal_print(s,s[i][j]+1,j)
        print(')',end='')

#print(m_in)
print(mcm(extract(m_in)))
#mcm_print(mcm(extract(m_in)))
#optimal_print(mcm(extract(m_in))[1],0,5)
