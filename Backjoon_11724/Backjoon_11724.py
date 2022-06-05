from collections import deque
import sys

input = sys.stdin.readline

node, edge = map(int,input().split())
graph = [[] for _ in range(node+1)]
visited_list = [False for _ in range(node+1)]
count = 0

def bfs(start):
    queue = deque()
    queue.append(start)
    visited_list[start] = True

    while queue:
        cur_node = queue.popleft()
        for i in graph[cur_node]:
            if visited_list[i] == False:
                queue.append(i)
                visited_list[i] = True

for _ in range(edge):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, len(visited_list)):
    if visited_list[i] == False:
        if not graph[i]:
            count += 1
            visited_list[i] = True
        else:
            bfs(i)
            count += 1

print(count)