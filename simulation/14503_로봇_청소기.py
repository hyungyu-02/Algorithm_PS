#Simulation
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

cleanedSec = 0

while True:
    if room[r][c] == 0:
        room[r][c] = -1
        cleanedSec += 1
    if room[r-1][c] == 0 or room[r][c+1] == 0 or room[r+1][c] == 0 or room[r][c-1] == 0:
        d -= 1
        if d < 0: d = 3
        if d == 0:
            if room[r-1][c] == 0:
                r -= 1
        elif d == 1:
            if room[r][c+1] == 0:
                c += 1
        elif d == 2:
            if room[r+1][c] == 0:
                r += 1
        elif d == 3:
            if room[r][c-1] == 0:
                c -= 1
    else:
        if d == 0:
            if not room[r+1][c] == 1:
                r += 1
            else:
                break
        elif d == 1:
            if not room[r][c-1] == 1:
                c -= 1
            else:
                break
        elif d == 2:
            if not room[r-1][c] == 1:
                r -= 1
            else:
                break
        elif d == 3:
            if not room[r][c+1] == 1:
                c += 1
            else:
                break
print(cleanedSec)
