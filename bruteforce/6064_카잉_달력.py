#bruteforce Algorithm, math
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    M, N, x, y = map(int, input().split())
    #K = M*p + x = N*q + y
    k = x
    if (k-x)%M == 0 and (k-y)%N == 0:
        print(k)
    else:
        while True:
            k += M
            if k > M*N:
                print(-1)
                break
            if (k-x)%M == 0 and (k-y)%N == 0:
                print(k)
                break
