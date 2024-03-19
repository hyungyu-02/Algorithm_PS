#data_structure, stack
inp = list(input())
stack = []

fir = ['*', '/']
sec = ['+', '-']
op = ['*', '/', '+', '-', '(', ')']

ans = ''

for s in inp:
    if s not in op:
        ans += s
    else:
        if s == '(':
            stack.append(s)
        elif s in fir:
            while stack and stack[-1] in fir:
                ans += stack.pop()
            stack.append(s)
        elif s in sec:
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
while stack:
    ans += stack.pop()
print(ans)
