#data structure
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
know = list(map(int, input().split()))
know.pop(0)
party = [list(map(int, input().split())) for _ in range(m)]
for row in party:
    row.pop(0)
num = 0
partyIdx = [i for i in range(m)]
trueParty = 0
while True:
    update = False
    for idx in partyIdx:
        for k in know:
            if k in party[idx]:
                know += party[idx]
                know = list(set(know))
                update = True
                partyIdx.remove(idx)
                trueParty += 1
                break
    if not update:
        break
print(m - trueParty)
