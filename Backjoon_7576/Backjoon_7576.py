from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
width,height = map(int, input().split())
store = []
queue = deque()
answer = 0
for _ in range(height):
    store.append(list(map(int,input().split())))

for i in range(len(store)):
    for j in range(len(store[i])):
        if store[i][j] == 1:
            queue.append((i,j))

while queue:
    cur_hei, cur_wid = queue.popleft()

    for i in range(4):
        new_hei = cur_hei + dx[i]
        new_wid = cur_wid + dy[i]

        if 0 <= new_hei < height and 0 <= new_wid < width and store[new_hei][new_wid] == 0:
            queue.append((new_hei, new_wid))
            store[new_hei][new_wid] = store[cur_hei][cur_wid] + 1

for i in store:
    for j in i:
        if j ==0:
            print(-1)
            exit(0)
    answer = max(answer, max(i))
print(answer-1)