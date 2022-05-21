test_iter = int(input())

for i in range(test_iter):
    print_num, print_target = map(int, input().split())
    print_priority = list(map(int, input().split()))
    print_queue = []
    count = 0

    print_list = []   
    for j in range(print_num):
        print_list.append(j)

    if print_num == 1:
        print('1')
        continue
    
    while print_priority:
        if not print_queue:
            print_queue.append(print_priority[0])
            print_queue.append(print_list[0])
            print_priority.pop(0)
            print_list.pop(0)
        for i in range(len(print_priority)):
            if print_queue[0] < print_priority[i]:
                print_priority.append(print_queue[0])
                print_list.append(print_queue[1])
                print_queue.clear()
                break
        else:
            count += 1
            if print_queue[1] == print_target:
                print(count)
                break
            print_queue.clear()