import random

# Greetings
print("""
          _______  ______   _______           _       
|\     /|(  ____ )(  __  \ (  ___  )|\     /|( (    /|
| )   ( || (    )|| (  \  )| (   ) || )   ( ||  \  ( |
| |   | || (____)|| |   ) || |   | || | _ | ||   \ | |
| |   | ||  _____)| |   | || |   | || |( )| || (\ \) |
| |   | || (      | |   ) || |   | || || || || | \   |
| (___) || )      | (__/  )| (___) || () () || )  \  |
(_______)|/       (______/ (_______)(_______)|/    )_)
                                                      

* 1에서 99 사이의 무작위 수를 맞춰보세요!
* 만약 생각한 숫자가 정답보다 작거나 크면 우리가 알려줄게요!
------------------------------------------------
""")

# generate random number
answer = random.randint(1, 99)

# life
life = 5

# repeat until correct
while True:
    # print life
    print('♥︎'*life + '♡'*(5-life))
    # user input
    guess = input('수를 입력하세요 (quit을 입력하면 종료) : ')
    if guess == 'quit':
        print('게임을 종료합니다.')
        break
    else:
        guess = int(guess)
    # up-down
    if guess < answer:
        print('UP!')
    elif guess > answer:
        print('DOWN!')
    else:
        print('정답입니다!')
        break
    # life
    life = life - 1
    if life == 0:
        print('실패하셨습니다...')
        break