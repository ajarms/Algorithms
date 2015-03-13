'''
prim's mst
'''
import random
import heapq
from GraphTools import Graph_m, Vertex_m, Edge_m, make_test



def mst_p(g):
    r = random.choice(g.v)
    for u in g.v:
        u.k = float('inf')
        u.parent = 0 
    r.k = 0
    Q = []          # priority queue
    for vert in g.v:
        heapq.heappush(Q, vert)
    edgelist = []   # return value
    while len(Q) > 0:
        Q.sort()
        u = heapq.heappop(Q)
        if u.parent != 0:
            edgelist.append(g.get_edge(u.parent,u))
        for v in g.adj(u):
            e = g.get_edge(u,v)
            if v in Q and e.w < v.k:
                v.parent = u
                v.k = e.w
    return edgelist
 



gt = make_test(0,1)

g = Graph_m(gt)

r = mst_p(g)

# mst_p returns an edgelist, now build a graph from that
mstg = Graph_m(0)   # 0 indicates empty graph
n = len(g.v)        # new graph will have same num verts as original
mstg.v = [Vertex_m(x,[Edge_m(x,y,0) for y in range(n)]) for x in range(n)]
for edge in r:      # fill in edges of mst
    mstg.v[edge.a].e[edge.b].w = edge.w
    mstg.v[edge.b].e[edge.a].w = edge.w 
    
w = mstg.to_string()

print('Original Non-Directed Graph:') 
print(gt+'\n')
print('Minimal-Spanning Tree:')
print(w)

