# https://school.programmers.co.kr/learn/courses/30/lessons/176962

def solution(plans):
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        plans[i][1] = h*60 + m
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x: x[1])
    
    answer = []
    stack = []
    
    for i in range(len(plans)):
        name, start, play_time = plans[i]
        
        if i > 0:
            prev_name, prev_start, prev_play_time = plans[i-1]
            available_time = start - prev_start
            
            while stack and available_time > 0:
                p_name, p_play_time = stack.pop()
                if p_play_time <= available_time:
                    answer.append(p_name)
                    available_time -= p_play_time
                else:
                    stack.append([p_name, p_play_time - available_time])
                    break
        
        stack.append([name, play_time])
    
    while stack:
        answer.append(stack.pop()[0])
    
    return answer

# 원래 내가 풀었던 풀이 (통과는 함)
"""
from collections import deque

def solution(plans):
    answer = []
    plans.sort(key=lambda x: x[1])
    
    for i in range(len(plans)):
        start_time = plans[i][1]
        h, m = map(int, start_time.split(':'))
        plans[i][1] = h*60 + m
        plans[i][2] = int(plans[i][2])
    
    new_plans = deque(plans)
    stack = deque()
    
    stack.append(new_plans.popleft())
    
    while stack:
        if not new_plans: break
        while stack and stack[-1][1] + stack[-1][2] <= new_plans[0][1]:
            end_plan = stack.pop()
            current_time = end_plan[1] + end_plan[2]
            if stack:
                for i in range(len(stack)):
                    stack[i][1] = current_time
            
            answer.append(end_plan[0])
        if stack:
            stack[-1][2] -= (new_plans[0][1] - stack[-1][1])
        stack.append(new_plans.popleft())
    
    if stack:
        while stack:
            end_plan = stack.pop()
            answer.append(end_plan[0])
            
    
    return answer
"""
