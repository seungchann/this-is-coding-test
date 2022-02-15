pos = input()
x, y = ord(pos[0])-96, int(pos[1])
answer = 0

dx = [-2, -1, 2, 1, -2, -1, 2, 1]
dy = [-1, -2, -1, -2, 1, 2, 1, 2]

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    answer += 1

print(answer)