from collections import deque

while True:
    count = 0
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    graph = []
    visited_list = [[False for i in range(N)] for j in range(M)]

    for _ in range(M):
        graph.append(list(map(int,input().split())))

    def bfs(x,y, visit_list):
        global count
        dx = [-1,1,0,0,-1,-1,1,1]
        dy = [0,0,-1,1,1,-1,1,-1]

        queue = deque()
        queue.append((x,y))
        if graph[x][y] == 1:
            graph[x][y] = 2

        visit_list[x][y] = True

        while queue:
            x, y = queue.popleft()
            for i in range(len(dx)):
                x_point = x + dx[i]
                y_point = y + dy[i]

                if x_point < 0 or x_point >= M or y_point < 0 or y_point >= N:
                    continue

                if graph[x_point][y_point] == 0:
                    continue

                if graph[x_point][y_point] == 1 and visit_list[x_point][y_point] == False:
                    graph[x_point][y_point] = 2
                    queue.append((x_point, y_point))
                    visit_list[x_point][y_point] = True
        count += 1
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                bfs(i,j, visited_list)

    print(count)
                