#완전탐색(BruteForce)
n, m = map(int, input().split())

result = []
board = []

for _ in range(n):
    board.append(input())


for i in range(n-7):
    for j in range(m-7):
        ca1 = 0
        ca2 = 0
        for r in range(8):
            for c in range(8):
                if ((r+c) % 2) == 0:
                    if board[i+r][j+c] == 'B':
                        ca1 += 1
                    else:
                        ca2 += 1
                else:
                    if board[i+r][j+c] == 'B':
                        ca2 += 1
                    else:
                        ca1 += 1
        result.append(ca1)
        result.append(ca2)
    
print(min(result))
