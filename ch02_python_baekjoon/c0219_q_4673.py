# self_nums = [False, False, False, ... False] -> False가 10001개
self_nums = []
for i in range(10001):
    self_nums.append(False)

# 브루트포스
for i in range(1, 10001):
    n = i
    N=[int(j) for j in str(n)]
    d_n = sum(N) + n
    if d_n <= 10000:
        self_nums[d_n] = True

# print answer
for i in range(1, 10001):
    if self_nums[i] == False:
        print(i)