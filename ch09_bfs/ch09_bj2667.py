from collections import deque

N = int(input())

# graph 만들기
graph = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

# 방향만들기
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 개수 리스트 만들기
cnts = []

# 모든 좌표에 대해서 시작할 노드로 설정
for i in range(N):
    for j in range(N):

        # 개수 변수 1로 만들기 (cnt = 1)
        cnt = 1

        # queue만들고 처음 시작할 노드 넣어주기
        queue = deque()

        if graph[i][j] == 0:
            continue
        if visited[i][j] == 1:
            continue
        queue.append((i, j))
        visited[i][j] = 1

        # queue가 빌 때까지 반복
        while queue:

            # popleft(), (x,y)
            x, y = queue.popleft()

            # 방향 4개에 대해서 (nx, ny)
            for d in range(4):
                nx, ny = x+dx[d], y+dy[d]

                # 1. (nx, ny)가 지도상에 존재하는지
                if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
                    continue

                # 2. (nx, ny) 지점에 node가 있는지
                if graph[nx][ny] == 0:
                    continue

                # 3. (nx, ny) 지점을 방문한 적이 있는지
                if visited[nx][ny] == 1:
                    continue

                # 위의 조건을 모두 통과했으면 visited 체크해주고, queue에 넣어준다. 
                queue.append((nx, ny))
                visited[nx][ny] = 1

                # 개수 + 1
                cnt += 1

        # 개수 리스트에 개수 넣어주기
        cnts.append(cnt)

# 개수 리스트 출력
print(cnts)
