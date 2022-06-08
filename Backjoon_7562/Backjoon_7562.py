from collections import deque
from sys import stdin
input = stdin.readline
dx = [2,2,-2,-2,1,1,-1,-1]
dy = [1,-1,1,-1,2,-2,2,-2]
test_iter = int(input())
for _ in range(test_iter):
    size = int(input())
    cur_point = list(map(int, input().split()))
    des_point = list(map(int, input().split()))
    stage = [[0] * size for _ in range(size)]
    queue = deque()
    queue.append(cur_point)
    stage[cur_point[0]][cur_point[1]] = 1
    while queue:
        cx, cy = queue.popleft()
        if cx == des_point[0] and cy == des_point[1]:
            break
        for i in range(8):
            nx,ny = cx + dx[i], cy + dy[i]
            if 0<=nx<size and 0<=ny<size and stage[nx][ny] == 0:
                stage[nx][ny] = stage[cx][cy] + 1
                queue.append([nx,ny])
    print(stage[des_point[0]][des_point[1]]-1)
