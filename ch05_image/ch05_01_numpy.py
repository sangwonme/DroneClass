import numpy as np

# Creating a 1D array
arr = np.array([1, 2, 3, 4, 5])

print(arr[3])
print(arr[2:4])

# Creating a 2D array
arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(arr[2, 1])
print(arr[0, 2])
print(arr[1, 0])

print(arr[0:2, 0:1])
print(arr[1:3, 0:2])
print(arr[:, 2])

print(arr.shape)

