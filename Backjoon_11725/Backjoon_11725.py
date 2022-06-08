from collections import deque
from sys import stdin
input = stdin.readline

node_num = int(input())
graph = [[] for _ in range(node_num+1)]
visited = [[False, 0] for _ in range(node_num+1)]
queue = deque()

for _ in range(node_num-1):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

queue.append(1)
visited[1][0] = True
visited[1][1] = 0
while queue:
    check = queue.popleft()
    for i in graph[check]:
        if not visited[i][0]:
            queue.append(i)
            visited[i][0] = True
            visited[i][1] = check

for i in range(2, node_num+1):
    print(visited[i][1])
