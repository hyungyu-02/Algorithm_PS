#백트래킹
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False]*(n)

grp = []

def bt():
    if len(grp) == m:
        print(' '.join(map(str, grp)))
        return
    avoidToStartWithMe = 0
    for i in range(len(arr)):
        if not visited[i] and avoidToStartWithMe != arr[i]:
            grp.append(arr[i])
            visited[i] = True
            avoidToStartWithMe = arr[i]
            bt()
            grp.pop()
            visited[i] = False
bt()
