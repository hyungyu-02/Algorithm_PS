#dijkstra, heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    adj[s].append((e,c))
start, end = map(int, input().split())
dijkstra = [1e9]*(n+1)
dijkstra[start] = 0
whereAmI = start
visited = [False]*(n+1)
visited[0] = True
visited[start] = True

while True:
    for to, cost in adj[whereAmI]:
        if not visited[to]:
            dijkstra[to] = min(dijkstra[to], dijkstra[whereAmI]+cost)
    compareCost = 1e9
    for i in range(1, n+1):
        if not visited[i]:
            if dijkstra[i] < compareCost:
                compareCost = dijkstra[i]
                whereAmI = i
    visited[whereAmI] = True
    if whereAmI == end:
        break
print(dijkstra[end])
