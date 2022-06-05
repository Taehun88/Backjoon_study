from collections import deque
MAX_SIZE = 100001
list_map = [1] * MAX_SIZE

n,k = map(int,input().split())
queue = deque()
queue.append(n)

while queue:
    cur_point = queue.popleft()
    if cur_point == k:
        break

    for i in [cur_point-1,cur_point+1,cur_point*2]:
        if 0<=i<MAX_SIZE and list_map[i] == 1:
            queue.append(i)
            list_map[i] = list_map[cur_point]+1

print(list_map[k]-1)
