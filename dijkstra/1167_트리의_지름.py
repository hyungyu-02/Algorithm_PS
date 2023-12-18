import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
V = int(input())
graph = [[] for _ in range(V+1)]
for i in range(1, V+1):
    temp = list(map(int, input().split()))
    head = temp.pop(0)
    temp.pop(-1)
    for j in range(0, len(temp), 2):
        graph[head].append((temp[j], temp[j+1]))
#

        
dist = [-1]*(V+1)
dist[1] = 0
def DFS(s, d):
    for nextV, nextD in graph[s]:
        if dist[nextV] == -1:
            dist[nextV] = d + nextD
            DFS(nextV, d + nextD)
    return

DFS(1, 0)
#V1 = dist.index(max(dist))
tmp = [0, 0]
for i in range(1, len(dist)):
    if dist[i] > tmp[1]:
        tmp[1] = dist[i]
        tmp[0] = i
dist = [-1]*(V+1)
dist[tmp[0]] = 0
DFS(tmp[0], 0)
print(max(dist))
