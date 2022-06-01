from collections import deque

com_num = int(input())
edge_num = int(input())

visited = [False for _ in range(com_num+1)]
com_connect = [[] for _ in range(com_num+1)]
print(com_connect)

for _ in range(edge_num):
    start, end = map(int, input().split())
    com_connect[start].append(end)
    com_connect[end].append(start)

def bfs(com_connect, start, visited, count):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()
        for i in com_connect[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1
    return count

vir_count = bfs(com_connect,1,visited,0)
print(vir_count)
