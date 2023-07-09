from collections import deque

# 게임 구역의 크기
N = int(input())

# 게임판의 맵
jellymap = [list(map(int, input().split())) for _ in range(N)]

# 각 칸 마다 방문 여부 (0=미방문, 1=방문)
visited = [[0 for _ in range(N)] for _ in range(N)]

# 방향
dx = [1, 0]
dy = [0, 1]

# queue 만들기
queue = deque()
queue.append((0, 0))
visited[0][0] = 1

# 성공 여부 변수
success = False

# BFS
while queue:
    # x, y
    x, y = queue.popleft()

    # nx, ny
    for i in range(2):
        # nx, ny 구하기
        nx, ny = x + dx[i]*jellymap[x][y], y + dy[i]*jellymap[x][y]

        # 경계체크
        if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
            continue

        # 방문여부체크
        if visited[nx][ny] == 1:
            continue

        # nx, ny 방문
        queue.append((nx, ny))
        visited[nx][ny] = 1

        # 성공 여부 체크
        if nx == N-1 and ny == N-1:
            success = True

if success:
    print('HaruHaru')
else:
    print('Hing')