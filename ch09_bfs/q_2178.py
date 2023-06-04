from collections import deque

N, M = map(int, input().split())

# maze 만들기
maze = [list(map(int, input())) for _ in range(N)]

# 1) 방향만들기
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 2) queue 만들기
queue = deque()
queue.append((0, 0))

# 3) BFS 만들기
while queue:
    # 3-1) pop
    x, y = queue.popleft()

    # 3-2) 붙어 있는 node 탐색하기
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i] # 붙어 있는 node의 좌표

        # 3-3) 이동할 수 없을 때, for문 skip
        # 3-3-1) maze 내부에 있는가
        if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
            continue
        # 3-3-2) 이동할 수 있는 길
        if maze[nx][ny] == 0:
            continue
        # 3-4) 이동 가능할 경우, queue에 넣음. 근데 이제 중복 체크 안하게
        if maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            queue.append((nx, ny))

print(maze[N-1][M-1])

