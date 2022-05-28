from collections import deque

N, M = map(int, input().split())
graph = []
is_visit = [[False for i in range(M)] for j in range(N)]


for _ in range(N):
    graph.append(list(map(int,input())))

def bfs(x,y,is_visit):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((x,y))
    is_visit[x][y] = True

    while queue:
        x,y = queue.popleft()
        for i in range(len(dx)):
            x_point = x + dx[i]
            y_point = y + dy[i]

            if x_point < 0 or x_point >= N or y_point < 0 or y_point >= M:
                continue

            if graph[x_point][y_point] == 0:
                continue

            if graph[x_point][y_point] == 1 and is_visit[x_point][y_point] == False:
                graph[x_point][y_point] = graph[x][y] + 1
                queue.append((x_point,y_point))
                is_visit[x_point][y_point] = True
            
    return graph[N-1][M-1]

print(bfs(0,0,is_visit))
