from collections import deque

N, M = map(int, input().split())

# 1) 방향설정
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

while N > 0 and M > 0:
    # make oceanmap
    oceanmap = [list(map(int, input().split())) for _ in range(M)]

    # 2) queue 만들기
    queue = deque()

    count = 0

    # 3) 모든 칸에 대해 BFS 돌려주기
    for i in range(M):
        for j in range(N):
            # 3-1) BFS에 land일 때 넣어줌
            if oceanmap[i][j] == 1:
                count += 1
                queue.append((i, j))

                # 4) BFS 시작
                while queue:
                    # 4-1) pop
                    x, y = queue.popleft()
                    oceanmap[x][y] = 2
                    # 4-2) 다음 좌표
                    for k in range(8):
                        nx, ny = x+dx[k], y+dy[k]
                        # 4-3) 범위확인, land 확인
                        if nx < 0 or ny < 0 or nx > M-1 or ny > N-1:
                            continue
                        if oceanmap[nx][ny] == 0:
                            continue
                        # 4-4) land인 경우
                        if oceanmap[nx][ny] == 1:
                            queue.append((nx, ny))

    print(count)
    N, M = map(int, input().split())