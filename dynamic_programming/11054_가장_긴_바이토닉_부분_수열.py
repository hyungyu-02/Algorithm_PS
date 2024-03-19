#Dynamic Programming, LIS
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
rA = A[::-1]

dpInc = [1 for _ in range(n)]
dpDec = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if A[i] > A[j]:
            dpInc[i] = max(dpInc[i], dpInc[j]+1)
#
for i in range(1, n):
    for j in range(i):
        if rA[i] > rA[j]:
            dpDec[i] = max(dpDec[i], dpDec[j]+1)
#
for i in range(n):
    dpInc[i] += dpDec[n-i-1]
print(max(dpInc)-1)
