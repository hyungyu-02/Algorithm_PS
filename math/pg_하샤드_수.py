# https://school.programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    x_sum = 0
    temp = x
    while temp > 0:
        x_sum += temp % 10
        temp //= 10
    
    return x % x_sum == 0
