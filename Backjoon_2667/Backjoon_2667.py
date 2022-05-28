from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x, y, graph):
    n = len(graph)
    part_count = 1
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 2

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            x_point = x + dx[i]
            y_point = y + dy[i]

            if x_point < 0 or x_point >= n or y_point < 0 or y_point >= n:
                continue
            
            if graph[x_point][y_point] == 1:
                graph[x_point][y_point] = 2
                queue.append((x_point, y_point))
                part_count += 1

    return part_count

square_length = int(input())
graph = []
part_count_list = []

for i in range(square_length):
    graph.append(list(map(int,input())))

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            part_count_list.append(bfs(i,j, graph))

part_count_list.sort()
print(len(part_count_list))
for i in part_count_list:
    print(i)