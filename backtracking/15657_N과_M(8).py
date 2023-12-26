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
        if grp:
            if grp[-1] <= i:
                grp.append(i)
                bt()
                grp.pop()
        else:
            grp.append(i)
            bt()
            grp.pop()

bt()
