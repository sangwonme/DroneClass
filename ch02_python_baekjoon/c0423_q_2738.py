A, B = [], []

N, M = map(int, input().split())

for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)

# TODO : 주어진 행렬 A, B의 행렬 덧셈 코드를 작성하시오

# STEP 1 : 코드 실행시키고 인풋 넣어본다음에 A, B가 어떻게 저장되고 있는지 확인해보기 (print 써서)
# print(A)
# print(B)

# STEP 2 : A + B = C
C = []
for i in range(N):
  row = []
  for j in range(M):
      row.append(A[i][j] + B[i][j])
  C.append(row)

print(C)