#DP 제목 : 구간 합 구하기 5
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [[0] for _ in range(N+1)]
board[0] += [0 for _ in range(N)]
for i in range(1, N+1):
    board[i] += list(map(int, input().split()))

for i in range(2, N+1):
    board[1][i] += board[1][i-1]
    board[i][1] += board[i-1][1]
for i in range(2, N+1):
    for j in range(2, N+1):
        board[i][j] = board[i][j] + board[i-1][j] + board[i][j-1] - board[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(board[x2][y2] - board[x1-1][y2] - board[x2][y1-1] + board[x1-1][y1-1])
