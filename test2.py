from scipy import stats
from itertools import permutations

def count_same_pos(r1, r2):
    cnt = 0
    for i in range(5):
        if(r1[i] == r2[i]):
            cnt += 1
    return cnt

x1 = ['a', 'b', 'c', 'd', 'e']

shuffled_x2 = permutations(x1)

distances = {}
for x2 in shuffled_x2:
    if(count_same_pos(x1, x2) == 1):
        dist = stats.kendalltau(x1, x2).correlation
        if dist not in distances:
            distances[dist] = []
        distances[dist].append(x2)

print(distances)