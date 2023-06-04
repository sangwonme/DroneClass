from collections import deque

N, M = map(int, input().split())


# 이동할 상, 하, 좌, 우 방향 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]


while N > 0 and M > 0:
    # make graph
    grpah = [list(map(int, input())) for _ in range(M)]

