def count_par(string):
    count_right = 0
    count_left = 0
    for i in range(len(string)):
        if string[i] == '(':
            count_right+=1
        else:
            count_left += 1
    if count_right - count_left != 0:
        return False
    else: return True

if __name__ == "__main__":
    iter_count = input()
    for iterate in range(int(iter_count)):
        string = input()
        print(string)
        isTrue = count_par(string)

        if isTrue:
            print("YES")
        else:
            print("NO")