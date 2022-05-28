from collections import deque
MAX_SIZE = 100001

current_loc, sister_loc = map(int, input().split())
visited_list = [-1] * MAX_SIZE
count = 0

def bfs(current_loc, visited_list):
    global count
    queue = deque([current_loc])
    visited_list[current_loc] = 0

    while queue:
        x_point = queue.popleft()

        if x_point == sister_loc:
            count += 1

        for i in [x_point-1, x_point+1, x_point*2]:
            if 0 <= i < MAX_SIZE:
                if visited_list[i] == -1 or visited_list[i] == visited_list[x_point] + 1:
                    visited_list[i] = visited_list[x_point] + 1
                    queue.append(i)

bfs(current_loc, visited_list)
print(visited_list[sister_loc])
print(count)