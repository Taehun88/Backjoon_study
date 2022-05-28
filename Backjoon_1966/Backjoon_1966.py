test_iter = int(input())

for i in range(test_iter):
    #입력 변수 선언 및 queue 선언
    #print_num은 프린트 할 문서의 개수
    #print_target는 내가 확인해야할 문서의 번호
    #print_priority는 프린트의 우선순위를 저장하는 list
    #print_queue는 출력되는 문서의 번호와 우선순위를 저장하는 list
    print_num, print_target = map(int, input().split())
    print_priority = list(map(int, input().split()))
    print_queue = []
    count = 0
    
    #print_list를 선언하고 초기화
    #print_list는 프린트 할 문서의 번호를 저장하는 list
    print_list = []   
    for j in range(print_num):
        print_list.append(j)

    #프린트 할 문서가 1개일 경우 1개만 나오면 되니 바로 1출력 후 반복 continue
    if print_num == 1:
        print('1')
        continue
    
    #print_priority가 비어있지 않을경우 반복
    while print_priority:
        #print_queue에 아무것도 없을때, print_queue에 우선순위와 문서번호를 저장
        if not print_queue:
            print_queue.append(print_priority[0])
            print_queue.append(print_list[0])
            print_priority.pop(0)
            print_list.pop(0)
        #print_priority를 순환하면서 print_queue에 들어있는 문서보다 우선순위가 높은 문서가 있는지 확인
        for i in range(len(print_priority)):
            if print_queue[0] < print_priority[i]:
                print_priority.append(print_queue[0])
                print_list.append(print_queue[1])
                print_queue.clear()
                break
        # 없을경우, print_queue를 flush 후, print_target와 문서번호를 비교, 같으면 반복문 종료
        # 다르면 print_count증가 후 재개
        else:
            count += 1
            if print_queue[1] == print_target:
                print(count)
                break
            print_queue.clear()