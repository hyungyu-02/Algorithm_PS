#백트래킹
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
numOfOp = list(map(int, input().split()))
add = numOfOp[0]
sub = numOfOp[1]
mul = numOfOp[2]
div = numOfOp[3]

maximun = -1e9
minimun = 1e9

def dfs(lev, res):
    global maximun, minimun, add, sub, mul, div
    if lev == n-1:
        maximun = max(res, maximun)
        minimun = min(res, minimun)
        return
    if add > 0:
        add -= 1
        dfs(lev+1, res + num[lev+1])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(lev+1, res - num[lev+1])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(lev+1, res * num[lev+1])
        mul += 1
    if div > 0:
        div -= 1
        dfs(lev+1, int(res / num[lev+1]))
        div += 1
    return
dfs(0, num[0])
print(maximun)
print(minimun)
