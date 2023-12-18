#dijkstra
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
for i in range(E):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

dist = [INF]*(V+1)

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0
    while q:
        d, now = heapq.heappop(q)
        if d > dist[now]:
            continue
        
        for adj in graph[now]:
            cost = d + adj[1]
            if cost < dist[adj[0]]:
                heapq.heappush(q, (cost, adj[0]))
                dist[adj[0]] = cost
                
dijkstra(start)
for i in range(1, V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
