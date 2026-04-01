# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    total_truck_num = len(truck_weights)
    
    bridge = deque([0] * bridge_length)
    arrived = 0
    curr_weight = 0
    p = 0
    time = 0
    while arrived < total_truck_num:
        time += 1
        out = bridge.popleft()
        if out > 0:
            arrived += 1
            curr_weight -= out
        
        if p < total_truck_num and truck_weights[p] + curr_weight <= weight:
            bridge.append(truck_weights[p])
            curr_weight += truck_weights[p]
            p += 1
        else:
            bridge.append(0)
        
    return time
