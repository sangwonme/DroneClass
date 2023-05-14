N = int(input())
slimes = list(map(int, input().split()))

slimes.sort(reverse=True)

score = 0

for i in range(len(slimes)-1):
    score = score + (slimes[i]*slimes[i+1])
    slimes[i+1] = slimes[i] + slimes[i+1]

print(score)