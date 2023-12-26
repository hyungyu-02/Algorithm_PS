#백트래킹
n, m = map(int, input().split())

source = list(map(int, input().split()))
source.sort()

grp = []

def bt():
    if len(grp) == m:
        print(' '.join(map(str, grp)))
        return
    for i in source:
        grp.append(i)
        bt()
        grp.pop()

bt()
