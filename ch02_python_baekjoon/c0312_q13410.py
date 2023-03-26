n, k  = map(int, input().split())

nums = []

for i in range(1, k+1):
    nums.append(int(str(i*k)[::-1]))

print(max(nums))