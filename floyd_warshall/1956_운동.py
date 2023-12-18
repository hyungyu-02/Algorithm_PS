#floyd-warshall
import sys
input = sys.stdin.readline
MAX = int(1e9)
V, E = map(int, input().split())
minCost = MAX

costInfo = [[MAX]*(V+1) for _ in range(V+1)]

for i in range(E):
    v1, v2, c = map(int, input().rstrip().split())
    costInfo[v1][v2] = c

for i in range(1, V+1):
    for j in range(1, V+1):
        for k in range(1, V+1):
            costInfo[i][j] = min(costInfo[i][j], costInfo[i][k]+costInfo[k][j])

for i in range(1,V+1):
    minCost = min(minCost, costInfo[i][i])
print(minCost if minCost != MAX else -1)
