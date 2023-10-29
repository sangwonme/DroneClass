n = input()

cnt = [0]*26

for i in range(len(n)):
    cnt[ord(n[i])-65] += 1

# 홀수 개수 만큼 있는 문자를 찾는다.
odd = []
for i in range(len(cnt)):
    if cnt[i] % 2 == 1:
        odd.append(chr(i+65))

# 홀수 개수인 문자가 2개 이상이면 불가능 (if)
if len(odd) >= 2:
    print("I'm Sorry Hansoo")

# 그게 아닌 경우 (else)
# cnt 개수만큼 'A'에서 'Z'까지 cnt[i]//2만큼 출력 하기 + 홀수개인 문자는 한번 출력 + 'Z'~'A'까지 cnt[i]//2만큼 출력
else:
    for i in range(26):
        print(chr(i+65)*(cnt[i]//2), end='')
    print(odd[0], end='')
    for i in range(26):
        print(chr((25-i)+65)*(cnt[25-i]//2), end='')