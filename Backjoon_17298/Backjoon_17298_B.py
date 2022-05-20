from collections import deque
from inspect import stack
import sys

list_len = int(input())
list_basis = list(map(int, sys.stdin.readline().split()))
save_stack = deque()
answer = [-1] * list_len

for i in range(list_len):
    while save_stack and list_basis[save_stack[-1]] < list_basis[i]:
        answer[save_stack.pop()] = list_basis[i]
    save_stack.append(i)

print(*answer)