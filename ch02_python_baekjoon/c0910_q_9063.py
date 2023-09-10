N = int(input())
xs = []
ys = []
for _ in range(N):
    x, y = list(map(int, input().split()))
    xs.append(x)
    ys.append(y)

width = max(xs) - min(xs)
height = max(ys) - min(ys)
print(width*height)
