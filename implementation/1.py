n = int(input())
crt_pos = [1,1]
move_list = list(input().split())

for i in move_list:
    if i == 'L':
        if crt_pos[1] == 1:
            continue
        else:
            crt_pos[1] -= 1
    elif i == 'R':
        if crt_pos[1] == n:
            continue
        else:
            crt_pos[1] += 1
    elif i == 'U':
        if crt_pos[0] == 1:
            continue
        else:
            crt_pos[0] -= 1
    # i == 'D'
    else:
        if crt_pos[0] == n:
            continue
        else:
            crt_pos[0] += 1

for i in crt_pos:
    print(i, end=" ")