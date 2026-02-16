# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):    
    number_str = list(map(str, numbers))
    
    number_str.sort(key=lambda x: x * 3, reverse=True)
    
    return str(int("".join(number_str)))
