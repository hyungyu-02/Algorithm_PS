#그래프 탐색(dfs), Tree
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, v = map(int, input().split())
    tree[p].append((c, v))
    tree[c].append((p, v))
#
cost = [-1]*(n+1)
def dfs(start, accum):
    for nxt, cst in tree[start]:
        if not cost[nxt] == -1:
            continue
        cost[nxt] = accum + cst
        dfs(nxt, accum+cst)
    return
cost[1] = 0
dfs(1, 0)
V1 = cost.index(max(cost))
cost = [-1]*(n+1)
cost[V1] = 0
dfs(V1, 0)
print(max(cost))
