'''
classes and methods to work with provided graph input
'''
import random



class Graph_m:
    # interpret string adj matrix as a graph, or make an empty graph
    def __init__(self, string):
        if string != False:
            s = string.split()
            for i in range(len(s)):
                s[i] = int(s[i])
            n = s[0]
            self.v = [Vertex_m(x,[Edge_m(x,y,0) for y in range(n)]) for x in range(n)]
            i,j = 0,0
            for x in range(2,len(s)):
                self.v[i].e[j].w = s[x]
                j += 1
                if j == n:
                    i,j = i+1,0
        else:
            self.v = []

    # turn graph back to printable string adj matrix
    def to_string(self):
        n = len(self.v)
        s = str(n)+'\n'
        for i in range(n):
            for j in range(n):
                s += str(self.v[i].e[j].w)
                if j < n-1:
                    s += ' '
                else:
                    s += '\n'
        return s

    # get set of vertices adjacent to a given vertex
    def adj(self, v):
        adj = []
        for edge in v.e:
            if edge.w != 0:
                adj.append(self.v[edge.b])
        return adj

    # check for an edge to a given vertex, return the edge or 0
    def get_edge(self, u, v):
        for edge in u.e:
            if self.v[edge.b] == v and edge.w != 0:
                return edge
        return 0




class Vertex_m:
    def __init__(self, key, elist):
        self.parent = None
        self.k = key
        self.e = []
        if elist != False:
            for edge in elist:
                self.e.append(edge)

    # overwrite '<' operator to enable priority queue
    def __lt__(self, other):
        return self.k < other.k


     

class Edge_m:
    def __init__(self, start, end, wt):
        self.w = wt
        self.a = start  # start and end are stored
        self.b = end    # as indexes, ie g.v[a].e[b]




# return an adjacency matrix as a string, directed or non, random or non
def make_test(directed=0, rand=0):
    if rand == False:
        # test inputs provided
        if directed == False:
            # non-directed graph
            g = "9\n 0  4  0  0  0  0  0  8  0\n 4  0  8  0  0  0  0 11  0\n 0  8  0  7  0  4  0  0  2\n 0  0  7  0  9 14  0  0  0  \n 0  0  0  9  0 10  0  0  0  \n 0  0  4 14 10  0  2  0  0 \n 0  0  0  0  0  2  0  1  6 \n 8 11  0  0  0  0  1  0  7\n 0  0  2  0  0  0  6  7  0"
        else:
            # directed graph
            g = "9\n0\n 0  4  8  3  0  0  0  0  0\n 0  0  3  0  5  0  0  0  0\n 0  0  0  0  7  2  0  0  0\n 0  0  4  0  0  0  10 0  0\n 0  0  0  0  0  0  0  6  0 \n 0  0  0  0  0  0 12  6  6 \n 0  0  0  0  0  0  0  0  9\n 0  2  0  0  0  0  0  0  1\n 0  0  0  4  0  0  0  2  0"
    else:
        # random test generator
        # max 9 nodes, small chance of returning unconnected graph
        n = random.randrange(3,10)  # num nodes in test graph
        w = ''  # weight placeholder
        ws = [0,0,0,0,0,1,2,3,4,5,6,7,8,9]  # weights; skewed for more 0's
        g = str(n) + '\n'   # return val, string of a graph
        s = random.randrange(0,n) # starting point vertex
        g += str(s) + '\n'
        for i in range(n):
            for j in range(n):
                if i == j:
                    w = '0'
                elif i > j:
                    opp = g[(j*n+i)*2+2]
                    if directed == False:
                        # non-directed graph
                        w = opp
                    else:
                        # directed graph
                        if int(opp) != 0:
                            w = '0'
                else:
                    w = str(random.choice(ws)) # random weight
                g += w
                if j != n-1:
                    g += ' '
                else:
                    g += '\n'

    return g    # return string, same format as provided input
