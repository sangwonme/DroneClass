import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

# 이미지 불러오기
dir_path = os.path.dirname(os.path.realpath(__file__))  # 현재 파일 위치
file_path = os.path.join(dir_path, 'img_tt.jpeg')       # 이미지 파일 위치
img = Image.open(file_path)                             # 이미지 파일 불러오기

# 이미지 numpy array로 저장하기
img_array = np.array(img)                               # 불러온 이미지를 numpy array로 저장

# sampled array
sampled_array = []

# TODO : down sampling
sampling_rate = 10
height = img_array.shape[0]
width = img_array.shape[1]

for i in range(height):
    if i % sampling_rate == 0:
        row = []
        for j in range(width):
            if j % sampling_rate == 0:
                row.append(img_array[i, j, :])
        sampled_array.append(row)

# sampled array to np array
sampled_array = np.array(sampled_array)



# .shape을 하면 이미지의 사이즈를 확인할 수 있음
print(sampled_array.shape)

# 이미지 show
plt.imshow(sampled_array)
plt.show()

print(sampled_array)