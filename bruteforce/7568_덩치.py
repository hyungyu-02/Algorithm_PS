#bruteforce Algorithm
n = int(input())
inf = []
score = [1]*n
for _ in range(n):
    x, y = map(int, input().split())
    inf.append((x,y))
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if inf[i][0] < inf[j][0] and inf[i][1] < inf[j][1]:
            score[i] += 1
for s in score:
    print(s, end = ' ')
