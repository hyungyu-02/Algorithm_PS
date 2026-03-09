# https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import Counter

def solution(k, tangerine):
    counts = Counter(tangerine)
    
    sorted_counts = sorted(counts.values(), reverse=True)
    
    answer = 0
    total = 0
    
    for c in sorted_counts:
        total += c
        answer += 1
        
        if total >= k:
            break
    
    return answer
