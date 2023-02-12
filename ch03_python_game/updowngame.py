import random

# 제목
print('''
 _ _  ___  __    _   _ _ _  _  _ 
| | || o \|  \  / \ | | | || \| |
| U ||  _/| o )( o )| V V || \\ |
|___||_|  |__/  \_/  \_n_/ |_|\_|

* 1~99 수 중 무작위 수를 맞춰보세요!
* 예측한 수가 정답과 다르면 저희가 알려드릴게요!

''')

# 무작위 수 생성
answer = random.randint(1, 99)
life = 5

# 게임 실행
while True:
    print('남은 횟수 : ', life)
    guess = int(input('수를 맞춰보세요 : '))
    if guess < answer:
        print('UP!')
    elif guess > answer:
        print('DOWN!')
    else:
        print('정답입니다!')
        break
    # 생명 깎기
    life = life - 1
    if life == 0:
        print('생명을 다 썼습니다.')
        break

