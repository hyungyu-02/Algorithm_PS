#Fibonacci, Matrix
dev = 1000000007
n = int(input())
def power(A, n):
    if n == 1:
        return A
    elif n % 2 == 0:
        return power(multi(A, A), n//2)
    else:
        return multi(power(A, n-1), A)
def multi(A, B):
    res = [[0]*len(B[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(B[0])):
            temp = 0
            for k in range(2):
                temp += A[i][k]*B[k][j]
            res[i][j] = temp % dev
    return res
init = [[1, 1], [1, 0]]
f1f2 = [[1], [1]]
if n < 3:
    print(1)
else:
    print(multi(power(init, n-2), f1f2)[0][0])
