#그래프 탐색(bfs, dfs)
import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)
dR = [0, 0, -1, 1, -1, -1, 1, 1]
dC = [-1, 1, 0, 0, -1, 1, -1, 1]
             
while True:
    w, h = map(int, read().split())
    if w == 0 and h == 0:
        break
    
    NOI = 0
    q = []
    land = []
    for _ in range(h):
        land.append(list(map(int, read().split())))
    visited = []
    visited = [[0 for _ in range(w)] for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if land[i][j] == 1 and visited[i][j] == 0:
                NOI += 1
                q.append([i,j])
                visited[i][j] = 1
                while q:
                    r, c = q[0]
                    q.pop(0)
                    for k in range(8):
                        nR = r + dR[k]
                        nC = c + dC[k]
                        if nR >= 0 and nR < h and nC >= 0 and nC < w:
                            if land[nR][nC] == 1 and visited[nR][nC] == 0:
                                q.append([nR,nC])
                                visited[nR][nC] = 1
    print(NOI)
