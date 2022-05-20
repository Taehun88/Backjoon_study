bar_laser = str(input())
bar_laser_replace = bar_laser.replace('()', '0')
answer = 0
bar_count = 0

for i in bar_laser_replace:
    if i == '0':
        answer += bar_count
    else:
        if i == "(":
            bar_count += 1
        else:
            answer += 1
            bar_count -= 1

print(answer)

