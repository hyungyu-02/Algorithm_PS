#Minimun Spanning Tree(MST), Kruskal Algorithm, Union-Find
import sys
input = sys.stdin.readline
V, E = map(int, input().split())
minCost = 0

eNc = [list(map(int, input().split())) for _ in range(E)]
eNc.sort(key=lambda x: x[2])

parent = [i for i in range(V+1)]

def getParent(v):
    if v == parent[v]:
        return v
    parent[v] = getParent(parent[v])
    return parent[v]

def unionParent(v1, v2):
    v1 = getParent(v1)
    v2 = getParent(v2)
    if v1 > v2:
        parent[v1] = v2
    else:
        parent[v2] = v1
    return

def isSameParent(v1, v2):
    return getParent(v1) == getParent(v2)

for v1, v2, c in eNc:
    if not isSameParent(v1, v2):
        unionParent(v1, v2)
        minCost += c
print(minCost)
