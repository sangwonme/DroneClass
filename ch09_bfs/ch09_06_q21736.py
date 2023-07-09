import sys; input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())
# 학교 지도
G = [list(map(str, list(input().strip()))) for _ in range(N)]

# 각 칸 마다 방문 여부 (0=미방문, 1=방문)
visited = [[0 for _ in range(M)] for _ in range(N)]

# dx, dy 만들기

# queue 만들기

# cnt 변수 만들기
cnt = 0

# BFS

# 답안 출력하기