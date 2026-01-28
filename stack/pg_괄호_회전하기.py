# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    def correctBracket(a):
        stack = []
        for bracket in a:
            if bracket == '(': stack.append(1)
            elif bracket == '{': stack.append(2)
            elif bracket == '[': stack.append(3)
            elif bracket == ')':
                if stack and stack[-1] == 1: stack.pop()
                else: return False
            elif bracket == '}':
                if stack and stack[-1] == 2: stack.pop()
                else: return False
            elif bracket == ']':
                if stack and stack[-1] == 3: stack.pop()
                else: return False
        return len(stack) == 0

    answer = 0
    for x in range(len(s)):
        string = s[x:] + s[:x]
        if correctBracket(string): answer += 1

    return answer
