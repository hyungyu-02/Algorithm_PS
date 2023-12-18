#Dijkstra, heapq
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
#
def dijkstra(start):
    cost = [INF]*(N+1)
    cost[start] = 0
    q = []
    heapq.heappush(q, (0, start)) #cost, 현재노드
    while q:
        cur_cost, cur_node = heapq.heappop(q)
        if cur_cost > cost[cur_node]:
            continue
        
        for i in graph[cur_node]:
            if cost[i[0]] > cur_cost + i[1]:
                cost[i[0]] = cur_cost + i[1]
                heapq.heappush(q, (cur_cost + i[1], i[0]))
    return cost
#
fromX = dijkstra(X)
maxTime = 0
for i in range(1, N+1):
    if i == X:
        continue
    maxTime = max(maxTime, fromX[i]+dijkstra(i)[X])
print(maxTime)
