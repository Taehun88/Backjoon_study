while(True):
    string = input()
    if string == ".":
        break
    stack = []
    is_True = True
    for i in string:
        if i == '(' or i == '[':
                stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                is_True = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack or stack[-1]=='(':
                is_True = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if is_True == True and not stack:
        print('yes')
    else:
        print('no')