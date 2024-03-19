#knapsack Algorithm
import sys
n, k = map(int, input().split())
items = [[0,0]]
knapsack = [[0 for _ in range(k+1)] for _ in range(n+1)]

for _ in range(n):
    items.append(list(map(int, input().split())))
    
for i in range(1, n+1):
    weight = items[i][0]
    value = items[i][1]
    for j in range(1, k+1):
        if j < weight:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(value + knapsack[i-1][j-weight], knapsack[i-1][j])
print(knapsack[n][k])
