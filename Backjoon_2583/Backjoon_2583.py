from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

height, width, num_square = map(int, input().split())
field_square = [[1 for _ in range(height)] for _ in range(width)]

for _ in range(num_square):
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            if field_square[i][j] == 1:
                field_square[i][j] = 0

def bfs(field, x, y):
    n = len(field)
    count = 1
    queue = deque()
    queue.append((x,y))
    field[x][y] = 2

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= width or ny < 0 or ny >= height:
                continue

            if field[nx][ny] == 1:
                field[nx][ny] = 2
                queue.append((nx,ny))
                count += 1
    return count

cnt = []
for i in range(len(field_square)):
    for j in range(len(field_square[i])):
        if field_square[i][j] == 1:
            cnt.append(bfs(field_square,i,j))

cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)
