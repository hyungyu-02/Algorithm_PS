# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    phone_book.sort()
    
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    
    return True

# hash를 이용한 풀이 - hash map의 조회 시간 복잡도는 O(1)
"""
def solution(phone_book):
    hash_map = {}
    
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    for phone_number in phone_book:
        temp = ""
        for num in phone_number[:-1]:
            temp += num
            if temp in hash_map:
                return False
    
    return True
"""
