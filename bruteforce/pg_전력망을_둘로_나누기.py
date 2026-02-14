# https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque

def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    for i, j in wires:
        graph[i].append(j)
        graph[j].append(i)
    
    
    def count_node(start_node, ignore_neighbor):
        queue = deque()
        visited = [False] * (n + 1)
        
        queue.append(start_node)
        visited[start_node] = True
        count = 1
        
        while queue:
            curr = queue.popleft()
            
            for neighbor in graph[curr]:
                if curr == start_node and neighbor == ignore_neighbor:
                    continue
                
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    count += 1
        
        return count
    
    difference = n
    
    for i, j in wires:
        cnt = count_node(i, j)
        difference = min(abs(2*cnt - n), difference)
    
    return difference
