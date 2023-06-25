import numpy as np
from PIL import Image
from collections import deque
from matplotlib import pyplot as plt
import time

TMP_ANS = False
idx = TMP_ANS
queue = TMP_ANS
threshold = 500
tmp = 0

# Load the image using PIL
image_pil = Image.open('bluesample_filt.png')  # Replace 'image.jpg' with the path to your image file

# Convert the PIL image to a NumPy array
img = np.array(image_pil)

# Q1) img는 np.array이다. print(img)를 실행해라.
print(img)
# Q2) img의 최대값과, img의 shape를 print해라.
print("Maximum value of img:", np.max(img))
print("Shape of img:", img.shape)
# Q3) 파란색인 칸의 개수를 print해라. (hint : np.count_nonzero() 함수를 검색해서 사용할 것)
blue_pixels = np.count_nonzero(img[:,:,2]>0)
print("Number of blue pixels:", blue_pixels)
# BFS
visited = [[0 for _ in range(img.shape[1])] for _ in range(img.shape[0])]
# Q4) visited의 shape를 print해라.
print("Shape of visited:", np.array(visited).shape)
# Q5) 방향 만들기 - dx, dy list를 만들어라.
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# Q6) idx = 0 으로 초기화 해주기
idx = 0


start_time = time.time()

# 각 픽셀에서 BFS 시작 여부 판단
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        pass

        # Q6) queue 만들기
        queue = deque()
        # Q7) img[i][j]는 [R, G, B]의 값을 가지는 리스트이다.
        #            (i, j) 위치의 픽셀이 검정색이 아니고, BFS에서 방문한적이 없으면 queue에 넣어주어라.
        if np.array_equal(img[i][j], [0, 0, 0]):
            continue
        if visited[i][j] != 0:
            continue
        queue.append((i, j))

        # idx 번호 키워주기
        idx += 1 if(queue) else 0

        # Q8) (i, j) 를 queue에 append한 이후라면 visited[i][j]의 값을 idx로 update하여라.
        visited[i][j] = idx

        # BFS 시작
        while queue:
            pass
            # Q9) queue에서 (x, y) 좌표를 popleft()해라.
            x, y = queue.popleft()

            # Q10) 방향 4개에 대하여 (nx, ny)를 for문으로 구하여라.
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
            
                # Q11-1) (nx, ny)가 이미지 좌표 안에 존재하는지
                if nx < 0 or ny < 0 or nx > img.shape[0]-1 or ny > img.shape[1]-1:
                    continue
                # Q11-2) (nx, ny) 지점에 색상이 채워져 있지 않으면 스킵
                if np.array_equal(img[nx][ny], [0, 0, 0]):
                    continue
                # Q11-3) (nx, ny) 지점에 방문한 적이 있으면 스킵
                if visited[nx][ny] != 0:
                    continue
                # Q12) 위의 조건을 모두 통과했으면 queue에 넣어주고, visited[nx][ny]의 값을 idx로 update하여라.
                queue.append((nx, ny))
                print('Visit : ({}, {})'.format(nx, ny))
                print(tmp)
                tmp += 1
                visited[nx][ny] = idx

# TODO : Q13) index의 최댓값 print하고 그리고 index의 최댓값이 무엇을 의미하는지 주석으로 작성하시오. (주석 쓰는 법 : # 하고 뒤에 글 치면 됨)
print('idx = ',idx)

# 여기서부터 정답 작성 -------------------------------------------------
# 
# 
# 
# 
# 
# 
# 
# 
# 
# -----------------------------------------------------------------


# TODO : Q14) 각 idx에 해당하는 칸이 몇칸 씩 있는지 print하시오. (hint : np.countnonzero() 이용할 것, for 문을 이용할 것)
visited = np.array(visited)
for i in range(idx+1):
    print('idx={} : {} cells'.format(i, np.count_nonzero(visited == i)))

# TODO : Q16) 가장 많은 칸을 보유한 idx에서, 해당 idx로 체크된 모든 칸들의 중심 좌표를 구하시오. (좌표 평균 구하면 됨)
indices = np.where(visited == 5)
c_x = int(indices[0].sum() / len(indices[0]))
c_y = int(indices[1].sum() / len(indices[1]))

# TODO : Q17) 가장 많은 칸을 보유한 idx에서, 해당 idx로 체크된 모든 칸들을 품을 수 있는 bounding box의 왼쪽 위 꼭지점의 좌표와 bounding box의 너비, 높이를 구하시오.
b_x = indices[0].min()
b_y = indices[1].min()
height = indices[0].max() - indices[0].min()
width = indices[1].max() - indices[1].min()

# TODO : Q18) img를 imshow()를 통해서 보여줄 건데, Q16과 Q17에서 구한 중심좌표와 bouding box를 함께 표시하시오.

plt.imshow(img)
# Draw the bounding box
bbox = plt.Rectangle((b_x, b_y), width, height,
                     fill=False, edgecolor='r', linewidth=2)
plt.gca().add_patch(bbox)
# Draw the dot
plt.plot(c_x, c_y, 'ro', markersize=5)
# Set axis labels and show the plot
plt.axis('off')
end_time = time.time()
plt.show()

# TODO : Q19) 이 프로그램이 실행되는데 걸리는 시간을 측정하시오.
# 주의 : 이 문제는 이 부분에 코드를 작성할 뿐만 아니라 윗부분에도 코드를 작성해야 한다.
# GPT 보다는 구글링을 통해 문제를 풀어보자.

elapsed_time = end_time - start_time
print("Elapsed time:", elapsed_time, "seconds")