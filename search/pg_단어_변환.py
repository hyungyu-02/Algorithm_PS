# https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque([(begin, 0)])
    visited = set([begin])

    while queue:
        current_word, dist = queue.popleft()

        if current_word == target:
            return dist

        for word in words:
            if word not in visited and is_changable(word, current_word):
                visited.add(word)
                queue.append((word, dist + 1))

    return 0

def is_changable(x, y):
    diff = sum(1 for a, b in zip(x, y) if a != b)
    return diff == 1
