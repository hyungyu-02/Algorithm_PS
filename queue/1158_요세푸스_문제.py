#Data_Structure, Queue
n, k = map(int, input().split())

arr = [i for i in range(1, n+1)]

answer = []
pnt = 0

for _ in range(n):
    pnt += k-1
    while pnt >= len(arr):
        pnt = pnt - len(arr)
    answer.append(str(arr.pop(pnt)))

print("<",", ".join(answer)[:],">", sep='')
