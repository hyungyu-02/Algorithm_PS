# https://school.programmers.co.kr/learn/courses/30/lessons/155651

import heapq

def solution(book_time):
    book_list = []
    for start, end in book_time:
        h, m = map(int, start.split(':'))
        start_time = h*60 + m
        
        h, m = map(int, end.split(':'))
        end_time = h*60 + m + 10
        
        book_list.append([start_time, end_time])
    
    book_list.sort()
    
    room_schedule = [] # 가장 빨리 끝나는 방 딱 하나만 빠르게 알면 되므로 최소 힙 구조 사용
    
    for start, end in book_list:
        if room_schedule and room_schedule[0] <= start:
            heapq.heappop(room_schedule)
        
        heapq.heappush(room_schedule, end)
    
    return len(room_schedule)
