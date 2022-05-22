from collections import deque
import collections

people_num, out_term = map(int, input().split())
queue = collections.deque(range(1, people_num+1))
out_num = []
count = 1

while queue:
    if count == out_term:
        out_num.append(queue.popleft())
        count = 1
    else:
        temp = queue.popleft()
        queue.append(temp)
        count += 1
    if len(queue) == 1:
        out_num.append(queue.pop())
print("<",end="")
for i in range(len(out_num)-1):
    print("%d,"%out_num[i], end=" ")
print(out_num[-1], end="")
print(">")