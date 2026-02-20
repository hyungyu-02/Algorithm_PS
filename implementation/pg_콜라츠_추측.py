# https://school.programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    if num == 1:
        return 0
    
    count = 0
    while count <= 500:
        count += 1
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        
        if num == 1:
            return count
    
    return -1
