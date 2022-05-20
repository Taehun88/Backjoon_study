import sys

list_len = int(input())
list_basis = list(map(int, sys.stdin.readline().split()))
answer = list_basis
index = 0

while(index < list_len):
    for i in range(index, list_len):
        if answer[index] < list_basis[i]:
            answer[index] = list_basis[i]
            break

    if answer[index] == list_basis[index]:
        answer[index] = -1
    index += 1


print(*answer)