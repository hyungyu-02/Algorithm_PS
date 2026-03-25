# https://school.programmers.co.kr/learn/courses/30/lessons/132265

from collections import Counter

def solution(topping):
    answer = 0
    set_a = set()
    cnt_b = Counter(topping)
    
    for t in topping:
        set_a.add(t)
        cnt_b[t] -= 1
        if cnt_b[t] <= 0:
            del cnt_b[t]
        
        if len(set_a) > len(cnt_b):
            break
        elif len(set_a) == len(cnt_b):
            answer += 1
        
    return answer
