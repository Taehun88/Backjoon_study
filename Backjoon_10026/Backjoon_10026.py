from collections import deque
from copy import deepcopy
from sys import stdin

input = stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]
count_nor = 0
count_abnor = 0

iter_line = int(input())
color_map = [list(input().rstrip()) for _ in range(iter_line)]
visited = [[0] * iter_line for _ in range(iter_line)]

def bfs(matrix, start):
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < iter_line and 0 <= ny < iter_line and matrix[nx][ny] == matrix[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx,ny))

for i in range(iter_line):
    for j in range(iter_line):
        if not visited[i][j]:
            bfs(color_map,(i,j))
            count_nor += 1

visited = [[0] * iter_line for _ in range(iter_line)]


for i in range(iter_line):
    for j in range(iter_line):
        if color_map[i][j] == 'G':
            color_map[i][j] = 'R'

for i in range(iter_line):
    for j in range(iter_line):
        if not visited[i][j]:
            bfs(color_map, (i,j))
            count_abnor += 1
print(count_nor, count_abnor)
