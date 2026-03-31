# https://school.programmers.co.kr/learn/courses/30/lessons/154538

from collections import deque

def solution(x, y, n):
    
    visited = {y}
    queue = deque([(y, 0)])
    
    while queue:
        curr, step = queue.popleft()
        if curr < x:
            continue
        if curr == x:
            return step
        
        if curr % 3 == 0:
            next_num = curr // 3
            if next_num not in visited:
                queue.append((next_num, step + 1))
                visited.add(next_num)
        
        if curr % 2 == 0:
            next_num = curr // 2
            if next_num not in visited:
                queue.append((next_num, step + 1))
                visited.add(next_num)
        
        if (curr - n) not in visited:
            queue.append((curr - n, step + 1))
            visited.add(curr - n)
    
    return -1
