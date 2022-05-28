N = int(input())
num_list = []

for i in range(N):
    write = int(input())
    if write == 0:
        num_list.pop()
    else:
        num_list.append(write)

print(sum(num_list))