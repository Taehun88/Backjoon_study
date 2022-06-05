from collections import deque
from sys import stdin
input = stdin.readline
dx,dy = [-1,1,0,0], [0,0,-1,1]

n, m = map(int,input().split())
map_maze = [list(map(int,input().strip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

def bfs(x,y,z):
    queue = deque()
    queue.append((x,y,z))
    while queue:
        a,b,t = queue.popleft()
        if a == n-1 and b == m-1:
            return visited[a][b][t]
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if map_maze[nx][ny] == 1 and t == 0:
                visited[nx][ny][1] = visited[a][b][0] + 1
                queue.append((nx,ny,1))
            elif map_maze[nx][ny] == 0 and visited[nx][ny][t] == 0:
                visited[nx][ny][t] = visited[a][b][t] + 1
                queue.append((nx,ny,t))
    return -1

print(bfs(0,0,0))