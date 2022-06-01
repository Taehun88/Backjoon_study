from collections import deque

test_iter = int(input())
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(hei, wid):
        queue = deque()
        queue.append((hei,wid))
        cabb_stage[hei][wid] = 2

        while queue:
            hei, wid = queue.popleft()

            for i in range(4):
                nhei = hei + dx[i]
                nwid = wid + dy[i]

                if 0 <= nhei < height and 0 <= nwid < width and cabb_stage[nhei][nwid] == 1:
                    cabb_stage[nhei][nwid] = 2
                    queue.append((nhei, nwid))

for _ in range(test_iter):
    width, height, cab_num = map(int, input().split())
    cabb_stage = [[0 for _ in range(width)] for _ in range(height)]
    cab_area = 0

    for _ in range(cab_num):
        wid, hei = map(int, input().split())
        cabb_stage[hei][wid] = 1

    for hei in range(height):
        for wid in range(width):
            if cabb_stage[hei][wid] == 1:
                bfs(hei, wid)
                cab_area += 1
    print(cab_area)