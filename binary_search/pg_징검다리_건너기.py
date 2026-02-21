# https://school.programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    left = 1
    right = 200000000
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        can_cross = True
        count = 0
        for stone in stones:
            if stone < mid:
                count += 1
            else:
                count = 0
            
            if count >= k:
                can_cross = False
                break
        
        if can_cross:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return answer
