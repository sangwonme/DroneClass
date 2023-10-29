n = int(input())

num = []

for i in range(n):
    num.append(int(input()))

num.sort()

print(sum(num)/n)
print(num[n//2])
print(max(num)-min(num))

# TODO : dict 만들어주기
count = {}

for i in range(n):
    # TODO : num[i] dict에 있으면 dict[num[i]] += 1
    if num[i] in count.keys():
        count[num[i]] += 1
    # TODO : num[i] dict에 없으면 num[i]: 1
    else:
        count[num[i]] = 1

# TODO : values 중에 최대인 값을 찾아서 key를 알아내야함. 
tmp = max(count.values())
keys = []
for k in count.keys():
    if count[k] == tmp:
        keys.append(k)

# TODO : values 중에 최대인 값이 여러개 있다면 key 중에서두번째로 작은 거
if len(keys) == 1:
    print(keys[0])
else:
    keys.sort()
    print(keys[1])