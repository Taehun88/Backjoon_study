from cmath import inf
import sys

list_len = int(input())
list_basis = list(map(int, sys.stdin.readline().split()))
answer = [-1] * list_len

for i in range(list_len -1):
    for j in range(i+1, list_len):
        if list_basis[i] < list_basis[j]:
            answer[i] = list_basis[j]
            break

print(*answer)
