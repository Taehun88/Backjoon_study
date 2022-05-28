init_string = input()
iter_num = int(input())
cursor = len(init_string)

for i in range(iter_num):
    order = input().split()
    if order[0] == 'P':
        init_string.insert(cursor, order[1])
    elif order[0] == "D":
        if cursor < len(init_string):
            cursor += 1
    elif order[0] == "L":
        if cursor > 0:
            cursor -= 1
    else:
        if cursor > 0:
            init_string.remove(init_string[cursor-1])

print(init_string)
