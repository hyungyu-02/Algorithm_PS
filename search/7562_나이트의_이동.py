#그래프 탐색(bfs), deque
from collections import deque
import sys
input = sys.stdin.readline
dC = [1,2,2,1,-1,-2,-2,-1]
dR = [2,1,-1,-2,-2,-1,1,2]

t = int(input())
for T in range(t):
    l = int(input())
    r, c = map(int, input().split())
    R, C = map(int, input().split())
    
    visited = [[0]*l for _ in range(l)]
    board = [[0]*l for _ in range(l)]
    
    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    
    while q:
        nr, nc = q.popleft()
        if nr == R and nc == C:
            print(board[R][C])
            break
        
        for i in range(8):
            nextR = nr + dR[i]
            nextC = nc + dC[i]
            if nextR >= 0 and nextR < l and nextC >= 0 and nextC < l and visited[nextR][nextC] == 0:
                q.append((nextR,nextC))
                board[nextR][nextC] = board[nr][nc] + 1
                visited[nextR][nextC] = 1
