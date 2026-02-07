# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    if n == 1 or n == 2:
        return 1
    
    answer = 1
    step = 3
    pieces = 2
    while True:
        if step > n: break
        
        if (n - step) % pieces == 0:
            answer += 1
        
        pieces += 1
        step += pieces
    
    return answer

# 다른 풀이 - 2포인터로 윈도우를 확장/축소 해가면서 답을 찾음
"""
def solution(n):
    answer = 0
    
    left, right = 1, 1
    current_sum = 1
    
    while left <= n:
        if current_sum < n:
            right += 1
            current_sum += right
        elif current_sum > n:
            current_sum -= left
            left += 1
        else:
            answer += 1
            current_sum -= left
            left += 1
    
    return answer
"""
