A, B = [], []

N, M = map(int, input().split())
for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)

M, K = map(int, input().split())
for row in range(M):
    row = list(map(int, input().split()))
    B.append(row)

# TODO
C = []

for i in range(N):
    row = []
    for j in range(K):
        e = 0
        for k in range(M):
            e = e + (A[i][k] * B[k][j])
        row.append(e)
    C.append(row)

print(C)