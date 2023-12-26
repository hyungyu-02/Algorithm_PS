#백트래킹, bruteforce algorithm, combinations
import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
minChiDist = int(1e9)

village = []
chi = []
home = []
for i in range(n):
    village.append(list(map(int, input().split())))
    for j in range(n):
        if village[i][j] == 1:
            home.append((i, j))
        elif village[i][j] == 2:
            chi.append((i, j))
#
dist = [[] for _ in range(len(chi))]
for i in range(len(chi)):
    cx, cy = chi[i]
    for hx, hy in home:
        dist[i].append(abs(cx-hx) + abs(cy-hy))
#
chiNum = [i for i in range(len(chi))]
chiDistFromEachHomes = [100 for _ in range(len(home))]
for i in range(1, m+1):
    combi = list(combinations(chiNum, i))
    for choice in combi:
        chiDistFromEachHomes = [100 for _ in range(len(home))]
        for chiIdx in choice:
            for homeIdx in range(len(home)):
                chiDistFromEachHomes[homeIdx] = min(chiDistFromEachHomes[homeIdx], dist[chiIdx][homeIdx])
        minChiDist = min(minChiDist, sum(chiDistFromEachHomes))
#
print(minChiDist)
