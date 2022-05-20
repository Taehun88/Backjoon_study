bar_laser = str(input())
answer = 0
bar_count = 0

for i in range(len(bar_laser)):
    if bar_laser[i] == "(":
        bar_count += 1
    else:
        if bar_laser[i-1] == "(":
            bar_count -= 1
            answer += bar_count
        else:
            answer += 1
            bar_count -= 1

print(answer)