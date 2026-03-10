# https://school.programmers.co.kr/learn/courses/30/lessons/131704

def solution(order):
    stack = []
    pointer = 0
    for i in range(1, len(order) + 1):
        stack.append(i)
        
        while stack and order[pointer] == stack[-1]:
            stack.pop()
            pointer += 1
    
    return pointer
