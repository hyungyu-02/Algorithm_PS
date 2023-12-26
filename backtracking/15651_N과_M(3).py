#백트래킹
n, m = map(int, input().split())
grp = []

def bt():
    if len(grp) == m:
        print(' '.join(map(str, grp)))
        return
    for i in range(1, n+1):
        grp.append(i)
        bt()
        grp.pop()

bt()
