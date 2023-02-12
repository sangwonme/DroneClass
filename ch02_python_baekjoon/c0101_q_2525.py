a, b = map(int, input().split())
d = int(input())

hour = d // 60
minute = d % 60

ans_hour = a + hour
ans_minute = b + minute

if b+minute >= 60:
    ans_hour = ans_hour + 1
    ans_minute = ans_minute - 60

print(ans_hour % 24, ans_minute)