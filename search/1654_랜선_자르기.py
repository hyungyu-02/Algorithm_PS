#binary search
import sys
input = sys.stdin.readline
k, n = map(int, input().split())
line = []
for i in range(k):
    line.append(int(input()))

start, end = 1, max(line)
while start <= end:
    mid = (start + end)//2
    num = 0
    for l in line:
        num += l // mid
    if num >= n:
        start = mid+1
    else:
        end = mid-1
print(end)
