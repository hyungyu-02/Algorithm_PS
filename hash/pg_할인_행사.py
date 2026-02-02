# https://school.programmers.co.kr/learn/courses/30/lessons/131127

from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    my_wish = Counter({w: n for w, n in zip(want, number)})
    
    for i in range(len(discount) - 9):
        current_window = Counter(discount[i:i+10])
        
        if my_wish == current_window:
            answer += 1
    
    return answer
# Hash와 슬라이딩 윈도우로 O(N) 최적화


"""
def solution(want, number, discount):
    answer = 0
    
    def count_num(item, index, discount):
        count = 0
        for i in range(10):
            if discount[index+i] == item:
                count += 1
        return count
    
    for i in range(len(discount) - 9):
        for j in range(len(want)):
            if count_num(want[j], i, discount) != number[j]:
                break
            
            if j == len(want) - 1:
                answer += 1
    
    return answer
"""
