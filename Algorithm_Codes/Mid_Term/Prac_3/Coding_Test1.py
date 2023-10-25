N, M = map(int, input().split())

info = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(1, N):
        info[i][j] += info[i][j - 1]

for i in range(1, N):
    for j in range(N):
        info[i][j] += info[i - 1][j]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    answer = info[x2 - 1][y2 - 1]

    if x1 > 1:
        answer -= info[x1 - 2][y2 - 1]
    if y1 > 1:
        answer -= info[x2 - 1][y1 - 2]

    if x1 > 1 and y1 > 1:
        answer += info[x1 - 2][y1 - 2]

    print(answer)
