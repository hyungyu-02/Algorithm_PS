#백트래킹
n, m = map(int, input().split())

grp = []

def bt():
    if len(grp) == m:
        print(' '.join(map(str, grp)))
        return
    for i in range(1, n+1):
        if i not in grp:
            grp.append(i)
            bt()
            grp.pop()

bt()
