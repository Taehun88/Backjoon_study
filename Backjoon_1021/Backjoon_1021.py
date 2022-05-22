from collections import deque
import collections

elem_num, target_num = map(int, input().split())
target_list = collections.deque(list(map(int, input().split())))
queue = collections.deque(range(1,elem_num+1))
count = 0

while True:
    if target_list[0] == queue[0]:
        target_list.popleft()
        queue.popleft()
    elif queue.index(target_list[0]) >= len(queue) / 2:
        temp = queue.pop()
        queue.insert(0, temp)
        count += 1
    elif queue.index(target_list[0]) < len(queue) / 2:
        temp = queue.popleft()
        queue.append(temp)
        count += 1
    if not target_list:
        break
print(count)
