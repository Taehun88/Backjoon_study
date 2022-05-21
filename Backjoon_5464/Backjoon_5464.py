price_iter, weight_iter = map(int, input().split())

price_list = [int(input()) for _ in range(price_iter)]
weight_list = [int(input()) for _ in range(weight_iter)]
list_queue = [int(input()) for _ in range(2*weight_iter)]
waiting_queue = []
parking_queue = [0] * price_iter
comming = 0

while True:
    if waiting_queue and parking_queue.count(0) != 0:
        for i in range(len(parking_queue)):
            if parking_queue[i] == 0:
                parking_queue[i] = waiting_queue[0]
                waiting_queue.pop(0)
                break
        continue

    if list_queue[0] < 0:
        comming += price_list[parking_queue.index(abs(list_queue[0]))] * weight_list[abs(list_queue[0])-1]
        parking_queue[parking_queue.index(abs(list_queue[0]))] = 0
        list_queue.pop(0)

    else:
        if len(list_queue) == 2*weight_iter:
            parking_queue[0] = list_queue[0]
            list_queue.pop(0)
        else:
            if parking_queue.count(0) != 0:
                for i in range(len(parking_queue)):
                    if parking_queue[i] == 0:
                        parking_queue[i] = list_queue[0]
                        list_queue.pop(0)
                        break
            else:
                waiting_queue.append(list_queue[0])
                list_queue.pop(0)
    if not list_queue:
        break

print(comming)        