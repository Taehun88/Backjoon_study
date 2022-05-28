count = 0
for i in range(int(input())):
    stack = []
    string = input()
    if len(string) % 2 != 0:
        continue
    else:
        for j in string:
            if not stack:
                stack.append(j)
            elif j == 'A':
                if stack[-1] == 'B':
                    stack.append(j)
                else:
                    stack.pop()
            elif j == 'B':
                if stack[-1] == "A":
                    stack.append(j)
                else:
                    stack.pop()
        if not stack:
            count += 1

print(count)