#queue
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n, f = map(int, input().split())
    q = list(map(int, input().split()))
    idx = [i for i in range(n)]
    turn = 0
    while q:
        if q[0] == max(q):
            q.pop(0)
            turn += 1
            if idx[0] == f:
                print(turn)
                break
            else:
                idx.pop(0)
        else:
            q.append(q.pop(0))
            idx.append(idx.pop(0))
