# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    n = len(prices)
    answer = [0] * n
    
    stack = []
    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            d_i = stack.pop()
            answer[d_i] = i - d_i
        
        stack.append(i)
    
    while stack:
        i = stack.pop()
        answer[i] = n - i - 1
    
    return answer
