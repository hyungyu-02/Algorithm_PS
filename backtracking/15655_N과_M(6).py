#백트래킹
n, m = map(int, input().split())

source = list(map(int, input().split()))
source.sort()

grp = []

def bt(idx):
    if len(grp) == m:
        print(' '.join(map(str, grp)))
        return
    for i in range(idx, len(source)):
        if source[i] not in grp:
            grp.append(source[i])
            bt(i)
            grp.pop()

bt(0)
