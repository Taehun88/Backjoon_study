from collections import deque
from re import T

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

chess_square = int(input())
chess_stage = [[1 for _ in range(chess_square)] for _ in range(chess_square)]
visited_list = [[False for _ in range(chess_square)]for _ in range(chess_square)]

cordinate_list=  list(map(int, input().split()))

current_point = (cordinate_list[0], cordinate_list[1])
end_point = (cordinate_list[2], cordinate_list[3])

def bfs(current):
    global visited_list
    global chess_stage
    queue = deque()
    queue.append(current)
    visited_list[current[0]][current[1]] = True
    

    while queue:
        x, y = queue.popleft()
        if x == end_point[0] and y == end_point[1]:
            break

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= chess_square or ny < 0 or ny >= chess_square:
                continue

            if visited_list[nx][ny] == True:
                continue

            if chess_stage[nx][ny] == 1 and visited_list[nx][ny] == False:
                queue.append((nx, ny))
                chess_stage[nx][ny] = chess_stage[x][y] + 1
                visited_list[nx][ny] = True

bfs(current_point)
if chess_stage[end_point[0]][end_point[1]] == 1:
    print(-1)
else:
    print(chess_stage[end_point[0]][end_point[1]] -1)