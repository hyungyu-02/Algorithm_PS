# https://school.programmers.co.kr/learn/courses/30/lessons/148653

def solution(storey):
    answer = 0
    
    while storey > 0:
        curr = storey % 10
        storey //= 10
        nxt = storey % 10
        
        if curr < 5:
            answer += curr
        elif curr > 5:
            answer += 10 - curr
            storey += 1
        else:
            answer += 5
            if nxt >= 5:
                storey += 1
    
    return answer
