# https://school.programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    answer = 0
    
    cache = deque(maxlen=cacheSize)
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            cache.remove(city)
            cache.appendleft(city)
            answer += 1
        else:
            cache.appendleft(city)
            answer += 5
    
    return answer
