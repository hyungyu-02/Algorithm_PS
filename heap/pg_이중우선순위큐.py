# https://school.programmers.co.kr/learn/courses/30/lessons/42628

import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    available = []
    count = 0
    
    for operation in operations:
        o, n = operation.split(' ')
        
        if o == 'I':
            heapq.heappush(min_heap, (int(n), count))
            heapq.heappush(max_heap, (-int(n), count))
            available.append(True)
            count += 1
        else:
            if n == '1':
                while max_heap and not available[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                
                if max_heap:
                    val, index = heapq.heappop(max_heap)
                    available[index] = False
            else:
                while min_heap and not available[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                
                if min_heap:
                    val, index = heapq.heappop(min_heap)
                    available[index] = False
    
    answer = []
    
    if any(available):
        while max_heap and not available[max_heap[0][1]]:
            heapq.heappop(max_heap)
        val, index = heapq.heappop(max_heap)
        answer.append(-val)
        
        while min_heap and not available[min_heap[0][1]]:
            heapq.heappop(min_heap)
        val, index = heapq.heappop(min_heap)
        answer.append(val)
        
        return answer
    
    return [0, 0]
