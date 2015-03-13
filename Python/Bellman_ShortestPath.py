'''
Bellman's Shortest Path Algorithm
'''
from GraphTools import Graph_m, Vertex_m, Edge_m, make_test


# Bellman-Ford Shortest-Path Algorithm
def sp_bf(G, n):
    #INIT SINGLE SOURCE
    s = g.v[n]                      # starting vertex
    for v in g.v:
        v.k = float('inf')          
        v.parent = 0
    s.k = 0

    for i in range(len(g.v)):
        #for edge (u,v) in g.e:
        for vertex in g.v:
            for e in vertex.e:
                if e.w > 0:              # edge exists
                    u = g.v[e.a]
                    v = g.v[e.b]
                    #RELAX (u,v,w)
                    if v.k > (u.k + e.w):   # check for any shorter paths
                        v.k = u.k + e.w     # update shortest path weight
                        v.parent = u        # set link back up the path
    for vertex in g.v:
            for e in vertex.e:
                if e.w > 0:
                    u = g.v[e.a]
                    v = g.v[e.b]
                    if v.k > u.k + e.w:
                        return False # graph contains negative cycles
    return True # graph's good, shortest paths found



# REPLACE TEST WITH YOUR CHOSEN STRING INPUT FOR GRADING
test = make_test(1,1)  # currently generating random directed graph
print(test)            # w/rand num vertices and rand starting point


start = int(test.split()[1])    # grab starting index
g = Graph_m(test)               # build graph from adj matrix string
r = sp_bf(g, start)             # run bellman-ford on it

if r == False:
    print('Infinitely short negative cycles found in graph')
else:
    # reconstruct from vertices modified by bellman-ford alg
    for i in range(len(g.v)):
        if i != start:
            l = g.v[i].k
            if l == float('inf'):
                print('No path from vertex {0} to vertex {1} exists'
                      .format(start,i))
            else:
                print('Shortest path from vertex {0} to vertex {1} is {2}'
                      .format(start,i,l))
            
