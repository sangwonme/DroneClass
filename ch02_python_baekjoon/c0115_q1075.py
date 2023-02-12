N = int(input())
F = int(input())

n = (N // 100) * 100

for i in range(100):
    if (n+i) % F == 0:
        print('%02d'%i)
        break
