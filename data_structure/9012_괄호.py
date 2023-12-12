#자료구조, stack
t = int(input())
score = 0

for i in range(t):
    score = 0
    vps = input()
    for j in range(len(vps)):
        if vps[j] == '(':
            score += 1
        else:
            score -= 1
        if score < 0:
            break
    if score == 0:
        print("YES")
    else:
        print("NO")
