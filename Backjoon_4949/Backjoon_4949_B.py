import re

string_list = list(input().split("."))
print(string_list)
regex_pattern = re.compile(r'[^ A-Za-z0-9가-힣+]')


for i in range(len(string_list)-1):
    checksum_small = 0
    checksum_large = 0
    change_string = regex_pattern.findall(string_list[i])
    print(change_string)
    for j in range(len(change_string)):
        if change_string[j] == '(':
            checksum_small += 1
        elif change_string[j] == ')':
            checksum_small -= 1
            if checksum_small < 0:
                print('no')
                break
        elif change_string[j] == '[':
            checksum_large += 1
        else:
            checksum_large -= 1
            if checksum_large < 0:
                print('no')
                break
    if checksum_large == 0 and checksum_small == 0:
        print('yes')
    else:
        print('no')
