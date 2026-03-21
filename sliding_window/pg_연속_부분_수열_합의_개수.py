# https://school.programmers.co.kr/learn/courses/30/lessons/131701

# 슬라이딩 윈도우를 사용해서 확장되는 부분'만' 더하면 되므로 O(N^2)으로 줄일 수 있음
def solution(elements):
    s = set()
    n = len(elements)
    
    for i in range(n):
        curr_sum = 0
        for w in range(n):
            curr_sum += elements[(i + w) % n]
            s.add(curr_sum)
    
    return len(s)


# 그냥 다 더해버리는 코드. O(N^3)에 가까움. 통과는 함.
def solution(elements):
    s = set()
    n = len(elements)
    elements = elements * 2
    
    for i in range(1, n + 1):
        for j in range(n):
            s.add(sum(elements[j:j+i]))
    
    return len(s)
