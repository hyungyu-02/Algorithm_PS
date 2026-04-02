# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    answer = 0
    move = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}
    hor = [[False] * 10 for _ in range(11)]
    ver = [[False] * 11 for _ in range(10)]
    
    dist = 0
    row = 5
    col = 5
    for dir in dirs:
        new_row = row + move[dir][0]
        new_col = col + move[dir][1]
        
        if new_row < 0 or new_row > 10 or new_col < 0 or new_col > 10:
            continue
        
        if dir == "U" and not ver[row-1][col]:
            ver[row-1][col] = True
            dist += 1
        elif dir == "D" and not ver[row][col]:
            ver[row][col] = True
            dist += 1
        elif dir == "R" and not hor[row][col]:
            hor[row][col] = True
            dist += 1
        elif dir == "L" and not hor[row][col-1]:
            hor[row][col-1] = True
            dist += 1
        
        row = new_row
        col = new_col
    
    return dist

# 다른 더 좋은 풀이
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2
