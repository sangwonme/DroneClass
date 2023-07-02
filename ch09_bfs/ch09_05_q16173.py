from collections import deque

# 게임 구역의 크기
N = int(input())

# 게임판의 맵
jellymap = [list(map(int, input().split())) for _ in range(N)]

# 각 칸 마다 방문 여부 (0=미방문, 1=방문)
visited = [[0 for _ in range(N)] for _ in range(N)]

# TODO : BFS를 이용한 문제 풀이
