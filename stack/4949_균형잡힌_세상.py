#Stack
while True:
    sen = input()
    if sen[0] == '.':
        break
    stack = []
    ans = "yes"
    
    for i in sen:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
    
    
    if stack:
        print('no')
    else:
        print('yes')
