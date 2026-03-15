# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    change_count = 0
    zero_count = 0
    
    while s != '1':
        ones = s.count('1')
        
        zero_count += len(s) - ones
        change_count += 1
        s = format(ones, 'b')
    
    return [change_count, zero_count]
