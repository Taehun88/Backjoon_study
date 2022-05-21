# Backjoon_1966 프린터 큐

* Logic
    > 프린트 순서를 담은 print_list를 0~print_num까지 초기화 한 후
    > print_queue에 순서대로 담는다
    > print_queue[0]과 print_priority를 비교하여 더 높은 순위가 있는지 확인 후
    > 더 높은 순위가 있다면 print_queue에 있는 print_num과 print_priority를 다시 print_list와 print_priority에 넣는다
    > 없다면, print_queue를 초기화 하고
    > print_queue[1]이 print_target와 동일한지 확인 후 동일하다면 종료

* Algorithm
    > Queue, Data structure
    