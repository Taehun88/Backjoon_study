from collections import deque
from sys import stdin
input = stdin.readline
rain_amount = 0
dx,dy = [-1,1,0,0], [0,0,-1,1]
size = int(input())
matrix = []
for _ in range(size):
    matrix.append(list(map(int, input().split())))
max_height = max(map(max, matrix))
visited = [[False] * size for _ in range(size)]
count_fix = 0

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < size and 0 <= ny < size and matrix[nx][ny] > rain_amount and visited[nx][ny] == False:
                queue.append((nx,ny))
                visited[nx][ny] = True

while rain_amount <= max_height:
    count_change = 0
    for i in range(size):
        for j in range(size):
            if not visited[i][j] and matrix[i][j] > rain_amount:
                bfs(i,j)
                count_change += 1
    if count_fix < count_change:
        count_fix = count_change
    rain_amount += 1
    visited = [[False] * size for _ in range(size)]

print(count_fix)

