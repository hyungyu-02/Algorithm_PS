# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    answer = -1
    move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    
    queue = deque([(0, 0, 1)])
    
    maps[0][0] = 0 # visited 말고 지나온 길을 벽으로 바꿔버리면 공간복잡도를 줄일 수 있다
    
    while queue:
        r, c, step = queue.popleft()
        
        if r == n - 1 and c == m - 1:
            answer = step
            break
        
        for i in range(4):
            next_r = r + move[i][0]
            next_c = c + move[i][1]
            if next_r < 0 or next_r >= n or next_c < 0 or next_c >= m:
                continue
            
            if maps[next_r][next_c] == 0:
                continue
            
            queue.append((next_r, next_c, step+1))
            maps[next_r][next_c] = 0
        
    return answer
