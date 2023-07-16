import time

n = 100

a = 0
b = 0
c = 0

t = time.time()

# O(n^2) 
for i in range(n):
    for j in range(n):
        a = a+1

print(time.time() - t)