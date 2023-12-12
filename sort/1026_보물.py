#정렬
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse = True)

ans = 0
for i in range(n):
    ans += A[i]*B[i]
print(ans)
