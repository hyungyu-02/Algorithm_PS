# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    answer = []
    left = right = len(sequence) - 1
    curr_sum = sequence[-1]
    while True:
        if curr_sum == k:
            if 0 < left and sequence[left-1] == sequence[right]:
                left -= 1
                right -= 1
                continue
            else:
                return [left, right]
        elif curr_sum < k:
            left -= 1
            curr_sum += sequence[left]
        else:
            right -= 1
            curr_sum -= sequence[right+1]
