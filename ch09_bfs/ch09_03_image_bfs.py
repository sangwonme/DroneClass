import numpy as np
from PIL import Image
from collections import deque

TMP_ANS = False
idx = TMP_ANS
queue = TMP_ANS

# Load the image using PIL
image_pil = Image.open('bluesample_filt.png')  # Replace 'image.jpg' with the path to your image file

# Convert the PIL image to a NumPy array
img = np.array(image_pil)

# TODO : Q1) img는 np.array이다. print(img)를 실행해라.
print(img)
# TODO : Q2) img의 최대값과, img의 shape를 print해라.
print("Maximum value of img:", np.max(img))
print("Shape of img:", img.shape)
# TODO : Q3) 파란색인 칸의 개수를 print해라. (hint : np.count_nonzero() 함수를 검색해서 사용할 것)
blue_pixels = np.count_nonzero(img[:,:,2]>0)
print("Number of blue pixels:", blue_pixels)
# BFS
visited = [[0 for _ in range(img.shape[1])] for _ in range(img.shape[0])]
# TODO : Q4) visited의 shape를 print해라.
print("Shape of visited:", np.array(visited).shape)
# TODO : Q5) 방향 만들기 - dx, dy list를 만들어라.
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# TODO : Q6) idx = 0 으로 초기화 해주기
idx = 0
# 각 픽셀에서 BFS 시작 여부 판단
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        pass

        # TODO : Q6) queue 만들기
        queue = deque()
        # TODO : Q7) img[i][j]는 [R, G, B]의 값을 가지는 리스트이다.
        #            (i, j) 위치의 픽셀이 검정색이 아니고, BFS에서 방문한적이 없으면 queue에 넣어주어라.
        if np.array_equal(img[i][j], [0, 0, 0]):
            continue
        if visited[i][j] != 0:
            continue
        queue.append((i, j))

        # idx 번호 키워주기
        idx += 1 if(queue) else 0

        # TODO : Q8) (i, j) 를 queue에 append한 이후라면 visited[i][j]의 값을 idx로 update하여라.
        visited[i][j] = idx

        # BFS 시작
        while queue:
            pass
            # TODO : Q9) queue에서 (x, y) 좌표를 popleft()해라.
            x, y = queue.popleft()

            # TODO : Q10) 방향 4개에 대하여 (nx, ny)를 for문으로 구하여라.
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
            
                # TODO : Q11-1) (nx, ny)가 이미지 좌표 안에 존재하는지
                if nx < 0 or ny < 0 or nx > img.shape[0]-1 or ny > img.shape[1]-1:
                    continue
                # TODO : Q11-2) (nx, ny) 지점에 색상이 채워져 있지 않으면 스킵
                if np.array_equal(img[nx][ny], [0, 0, 0]):
                    continue
                # TODO : Q11-3) (nx, ny) 지점에 방문한 적이 있으면 스킵
                if visited[nx][ny] != 0:
                    continue
                # TODO : Q12) 위의 조건을 모두 통과했으면 queue에 넣어주고, visited[nx][ny]의 값을 idx로 update하여라.
                queue.append((nx, ny))
                print('Visit : ({}, {})'.format(nx, ny))
                visited[nx][ny] = idx

# TODO : Q13) index의 최댓값 print하고 그리고 index의 최댓값이 무엇을 의미하는지 주석으로 작성하시오. (주석 쓰는 법 : # 하고 뒤에 글 치면 됨)
print(idx)