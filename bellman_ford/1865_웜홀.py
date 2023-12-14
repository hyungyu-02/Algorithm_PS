#bellman-ford algorithm
import sys
input = sys.stdin.readline
INF = int(1e9)
TC = int(input())

def bf():
    yes = False
    n, m, w = map(int, input().split())
    info = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        info.append((s, e, t))
        info.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        info.append((s, e, t*(-1)))
    #
    dist = [INF]*(n+1)
    dist[1] = 0
    for i in range(n):
        for s, e, t in info:
            if dist[e] > t + dist[s]:
                dist[e] = t + dist[s]
                if i == n-1:
                    yes = True
                    break
    if yes:
        print("YES")
    else:
        print("NO")
    return
for _ in range(TC):
    bf()
