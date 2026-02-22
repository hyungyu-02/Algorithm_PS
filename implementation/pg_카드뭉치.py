# https://school.programmers.co.kr/learn/courses/30/lessons/159994

def solution(cards1, cards2, goal):
    pointer1 = 0
    pointer2 = 0
    for word in goal:
        if pointer1 < len(cards1) and cards1[pointer1] == word:
            pointer1 += 1
        elif pointer2 < len(cards2) and cards2[pointer2] == word:
            pointer2 += 1
        else:
            return "No"
    return "Yes"
