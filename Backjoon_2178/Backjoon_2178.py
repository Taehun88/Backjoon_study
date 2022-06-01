from collections import deque

N, M = map(int, input().split())
graph = []
is_visit = [[False for i in range(M)] for j in range(N)]


for _ in range(N):
    graph.append(list(map(int,input())))

def bfs(x,y,is_visit):
    dx = [-1,1,0,0] # 좌우를 탐색하기 위한 배열
    dy = [0,0,-1,1] # 상하를 탐색하기 위한 배열

    queue = deque() # 탐색할 지점을 저장하기 위한 queue 선언
    queue.append((x,y)) # 시작점
    is_visit[x][y] = True # 시작점을 방문했다는 표시

    while queue:
        x,y = queue.popleft() # 탐색할 지점을 저장
        for i in range(len(dx)): # 사방탐색 시작점
            x_point = x + dx[i]
            y_point = y + dy[i]

            if x_point < 0 or x_point >= N or y_point < 0 or y_point >= M: # 주어진 배열보다 넘어갈 경우 pass
                continue

            if graph[x_point][y_point] == 0: # 탐색 불가 지역일 경우 pass
                continue

            if graph[x_point][y_point] == 1 and is_visit[x_point][y_point] == False: # 탐색 가능이면서 방문기록 없으면 동작
                graph[x_point][y_point] = graph[x][y] + 1 # 최단거리이기 때문에 전 지점 + 1로 기록
                queue.append((x_point,y_point)) # 다음 칸으로 움직이기 위해 queue에 insert
                is_visit[x_point][y_point] = True # 방문기록 업데이트
            
    return graph[N-1][M-1]

print(bfs(0,0,is_visit))
