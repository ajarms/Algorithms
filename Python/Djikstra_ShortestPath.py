'''
djikstra's Shortest Path algorithm
'''
import random
import heapq
from GraphTools import Graph_m, Vertex_m, Edge_m, make_test




# djikstra's shortest path algorithm, single point to all points
def sp_d(g, n):
    s = g.v[n]                      # starting vertex
    for v in g.v:
        v.k = float('inf')          # setup starting values
        v.parent = 0
    s.k = 0
    S = []                          # list of SP endpoints
    Q = []                          # priority queue of vertices
    for vert in g.v:
        heapq.heappush(Q, vert)     # load vertices into queue
    while len(Q) > 0:
        Q.sort()
        u = heapq.heappop(Q)        # grab shortest-path vertex
        if u not in S:
            S.append(u)             # add it to the endpoint list
        for v in g.adj(u):
            e = g.get_edge(u,v)
            if v.k > (u.k + e.w):   # check for any shorter paths
                v.k = u.k + e.w
                v.parent = u        # set link back up the path
 
    return (S, g, n)                # feed this to print_sp




# prints each shortest path generated by sp_d, as an adjacency matrix
def print_sp(sp):
    S, g, n = sp                            # unpack
    for p in S:
        if p.k != 0 and p.k != float('inf'):# exclude non-paths
            m = p.e[0].a                    # get vertex index
            w = p.k
            path = Graph_m(0)               # make edge-less graph
            path.v = [Vertex_m(x,[Edge_m(x,y,0)
                      for y in range(len(g.v))])
                      for x in range(len(g.v))]
            while p.parent != 0:            # stop at starting vertex
                e = g.get_edge(p.parent, p)
                path.v[e.a].e[e.b].w = e.w  # put path edges into graph
                p = p.parent                
            pr = path.to_string()           # make printable
            print ("Shortest Path from Vertex {0} to Vertex {1}:"
                   .format(n+1, m+1))       # print path identity
            print ('Path Length {0}\n'
                   .format(w) + pr)         # print graph




gt = make_test(1)

g = Graph_m(gt)

r = sp_d(g, 0)

print('Original Directed Graph:')
print(gt,'\n')
print_sp(r)
