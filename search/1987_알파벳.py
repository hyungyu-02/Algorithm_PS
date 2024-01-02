#그래프 탐색(dfs)
import sys
input = sys.stdin.readline

dR = [0, 0, -1, 1]
dC = [-1, 1, 0, 0]
r, c = map(int, input().split())
board = [list(map(lambda x:ord(x)-65, input().strip())) for _ in range(r)]
#

alp = [False]*26
maxVal = 0

def DFS(curR, curC, cnt):
    global maxVal
    
    spread = False
    for i in range(4):
        nr, nc = curR + dR[i], curC + dC[i]
        if 0 <= nr < r and 0 <= nc < c:
            if not alp[board[nr][nc]]:
                alp[board[nr][nc]] = True
                DFS(nr, nc, cnt+1)
                alp[board[nr][nc]] = False
                spread = True
    ##
    if not spread:
        maxVal = max(maxVal, cnt)
    return

alp[board[0][0]] = True
DFS(0, 0, 1)
print(maxVal)
