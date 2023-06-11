from collections import deque

N = int(input())

# graph 만들기
graph = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

# TODO : 방향만들기

# 개수 리스트 만들기
cnts = []

# TODO : 모든 좌표에 대해서 시작할 노드로 설정
for i in range(N):
    for j in range(N):

        # 개수 변수 1로 만들기 (cnt = 1)
        cnt = 1

        # TODO : queue만들기

        # TODO : graph (i, j)위치에 노드가 있고 방문한 적이 없으면 queue에 넣어주고 visited 체크해주기
        

        # TODO : queue가 빌 때까지 반복

            # TODO : popleft(), (x,y)
            

            # TODO : 방향 4개에 대해서 (nx, ny)

                # TODO : 1. (nx, ny)가 지도상에 존재하는지
                

                # TODO : 2. (nx, ny) 지점에 node가 있는지
                

                # TODO : 3. (nx, ny) 지점을 방문한 적이 있는지
                
                # TODO : 위의 조건을 모두 통과했으면 visited 체크해주고, queue에 넣어준다. 
                
                # TODO : 개수 + 1
                

        # 개수 리스트에 개수 넣어주기
        cnts.append(cnt)

# 개수 리스트 출력
print(cnts)
