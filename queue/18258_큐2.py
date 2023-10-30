#deque
import sys
from collections import deque
n = int(input())
qu = deque([])
for _ in range(n):
    op = sys.stdin.readline().split()
    if op[0] == "push":
        qu.append(op[1])
    elif op[0] == "pop":
        if len(qu) != 0:
            print(qu.popleft())
        else:
            print(-1)
    elif op[0] == "size":
        print(len(qu))
    elif op[0] == "empty":
        if len(qu) != 0:
            print(0)
        else:
            print(1)
    elif op[0] == "front":
        if len(qu) != 0:
            print(qu[0])
        else:
            print(-1)
    else:
        if len(qu) != 0:
            print(qu[-1])
        else:
            print(-1)
