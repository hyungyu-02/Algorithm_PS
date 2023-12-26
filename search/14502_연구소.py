#탐색(bfs), brutefoce algorithm
import sys
from collections import deque
input = sys.stdin.readline

dR = [0, 0, -1, 1]
dC = [-1, 1, 0, 0]

maxSafeArea = 0

n, m = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(n)]

initVirusPos = []
initWallNum = 0

for i in range(n):
    for j in range(m):
        if lab[i][j] == 2:
            initVirusPos.append((i, j))
        elif lab[i][j] == 1:
            initWallNum += 1

def bfs():
    global maxSafeArea
    visited = [[False for _ in range(m)] for _ in range(n)]
    virusOccupNum = 0
    q = deque()
    for r, c in initVirusPos:
        q.append((r, c))
        visited[r][c] = True
    #
    while q:
        r, c = q.popleft()
        virusOccupNum += 1
        for i in range(4):
            row = r + dR[i]
            col = c + dC[i]
            if row >= 0 and row < n and col >= 0 and col < m:
                if lab[row][col] == 0 and not visited[row][col]:
                    q.append((row, col))
                    visited[row][col] = True
    maxSafeArea = max(maxSafeArea, n*m - initWallNum - virusOccupNum - 3)
    return

def makeWall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                makeWall(cnt+1)
                lab[i][j] = 0
    return
makeWall(0)
print(maxSafeArea)
