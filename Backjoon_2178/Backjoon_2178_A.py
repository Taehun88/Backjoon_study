from re import S


start_point = (0, 0)
dx = [1,1,0]
dy = [1,0,1]

route_save_list = []
route_save_list.append(start_point)

height, width = map(int, input().split())
graph = []
for _ in range(height):
    graph.append(list(map(int, input())))

visit_list = [[False for _ in range(width)] for _ in range(height)]
visit_list[start_point[0]][start_point[1]] = True

while True:
    current_point = route_save_list[-1]
    current_length = len(route_save_list)
    if current_point == (width-1, height-1):
        print(len(current_point))
        break
    
    for i in range(3):
        nx = current_point[0] + dx[i]
        ny = current_point[1] + dy[i]

        if nx >= width or nx >= height:
            continue
        elif graph[nx][ny] == 0:
            continue