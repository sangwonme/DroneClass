import numpy as np

A, B = [], []

N, M = map(int, input().split())

for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)


# without numpy
C = []
for i in range(N):
  row = []
  for j in range(M):
      row.append(A[i][j] + B[i][j])
  C.append(row)

# with numpy
A = np.array(A)
B = np.array(B)
C = A + B

print(C)


# ------------------------------------------
A, B = [], []

N, M = map(int, input().split())
for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)

M, K = map(int, input().split())
for row in range(M):
    row = list(map(int, input().split()))
    B.append(row)

# without numpy
C = []
for i in range(N):
    row = []
    for j in range(K):
        e = 0
        for k in range(M):
            e = e + (A[i][k] * B[k][j])
        row.append(e)
    C.append(row)

# with numpy
A = np.array(A)
B = np.array(B)
C = np.matmul(A, B)

print(C)