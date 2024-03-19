#bruteforce Algorithm
import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]
highest = max(max(ground))
lowest = min(min(ground))

time = int(1e9)
height = 0

for h in range(lowest, highest+1):
    use = 0
    get = 0
    
    for i in range(n):
        for j in range(m):
            if ground[i][j] > h:
                get += (ground[i][j] - h)
            else:
                use += (h - ground[i][j])
    if b + get < use:
        continue
    needTime = use + get*2
    if time >= needTime:
        time = needTime
        height = h
print(time, height)
