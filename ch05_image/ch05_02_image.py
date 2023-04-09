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

# .shape을 하면 이미지의 사이즈를 확인할 수 있음
print(img_array.shape)

# 이미지 show
plt.imshow(img_array)
plt.show()