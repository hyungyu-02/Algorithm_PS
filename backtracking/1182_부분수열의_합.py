#백트래킹
#itertools 사용
import sys
from itertools import combinations
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(1, n+1):
    temp = combinations(arr, i) #전체수열, 부분수열의 크기
    
    for seq in temp:
        if sum(seq) == s:
            ans += 1
print(ans)
