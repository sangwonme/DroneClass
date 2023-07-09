import sys; input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())
# 학교 지도
G = [list(map(str, list(input().strip()))) for _ in range(N)]

# 각 칸 마다 방문 여부 (0=미방문, 1=방문)
visited = [[0 for _ in range(M)] for _ in range(N)]

# dx, dy 만들기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# I 위치 알아내기
sx = 0
sy = 0
for i in range(N):
    for j in range(M):
        # 만약 G의 해당 좌표가 'I'면 sx=i, sy=j
        if G[i][j] == 'I':
            sx, sy = i, j

# queue 만들기
queue = deque()
queue.append((sx, sy))
visited[sx][sy] = 1

# cnt 변수 만들기
cnt = 0

# BFS
while queue:
    x, y = queue.popleft()

    # nx, ny
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
            continue

        if G[nx][ny] == 'X':
            continue

        if visited[nx][ny] == 1:
            continue

        queue.append((nx, ny))
        visited[nx][ny] = 1

        if G[nx][ny] == 'P':
            cnt += 1

# 답안 출력하기
if cnt == 0:
    print('TT')
else:
    print(cnt)