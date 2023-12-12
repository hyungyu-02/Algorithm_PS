#그래프 탐색(bfs, dfs), tree
import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
parent = [0]*(n+1)
q = []
q.append(1)
while q:
    node = q.pop()
    for i in graph[node]:
        if parent[i] == 0:
            q.append(i)
            parent[i] = node
for p in parent[2:]:
    print(p)
