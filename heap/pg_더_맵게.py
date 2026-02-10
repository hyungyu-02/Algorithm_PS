# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while scoville[0] < K and 2 <= len(scoville):
        min_s = heapq.heappop(scoville)
        min_s2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min_s + min_s2*2)
        answer += 1
    
    if K <= heapq.heappop(scoville):
        return answer
    else:
        return -1
