row, col = map(int, input().split())
x, y, direction = map(int, input().split())
map = list(list(map(int, input().split())) for _ in range(col))
answer = 1
cannot_move = [False, False, False, False]

# 움직인 정도
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

map[x][y] = 1
# print("map[" + str(x) + "][" + str(y) + "]")

while(1):
    # 먼저 왼쪽 방향으로 회전
    direction -= 1
    if direction < 0:
        direction = 3

    nx = x + dx[direction]
    ny = y + dy[direction]

    # 육지라면
    if map[nx][ny] == 0:
        x = nx
        y = ny
        answer += 1
        # print("map[" + str(nx) + "][" + str(ny) + "]")
        map[nx][ny] = 1
    
    # 갈수 없는 칸이라면
    else:
        cannot_move[direction] = True

    # 네 방향 모두 갈 수 없는 칸이라면
    if cannot_move == [True, True, True, True]:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if map[nx][ny] == 0:
            x = nx
            y = ny
            answer += 1
            # print("map[" + str(nx) + "][" + str(ny) + "]")
            map[nx][ny] = 1
        else:
            break

print(answer)