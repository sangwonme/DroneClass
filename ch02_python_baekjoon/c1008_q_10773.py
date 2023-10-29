k = int(input())

# TODO : list 만들기
nums = []

for i in range(k):
    n = int(input())
    # TODO : n이 0인지 아닌지에 따라 추가 / 삭제
    if n == 0:
        nums.pop()
    else:
        nums.append(n)

# TODO : 합 출력
print(sum(nums))