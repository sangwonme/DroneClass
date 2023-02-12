import random

print('''

.88b  d88.  .d88b.   .d88b.  db   dD    .o88b. db   db d888888b   d8888b. d8888b.  .d8b.  
88'YbdP`88 .8P  Y8. .8P  Y8. 88 ,8P'   d8P  Y8 88   88   `88'     88  `8D 88  `8D d8' `8b 
88  88  88 88    88 88    88 88,8P     8P      88ooo88    88      88oodD' 88oodD' 88ooo88 
88  88  88 88    88 88    88 88`8b     8b      88~~~88    88      88~~~   88~~~   88~~~88 
88  88  88 `8b  d8' `8b  d8' 88 `88.   Y8b  d8 88   88   .88.     88      88      88   88 
YP  YP  YP  `Y88P'   `Y88P'  YP   YD    `Y88P' YP   YP Y888888P   88      88      YP   YP 
                                                                                                                                                                                    
''')

computer = random.choice(['묵', '찌', '빠'])
print('------------------------------------')
me = input('묵찌빠 중 하나를 입력하세요 : ')

# 처음 공격권 결정
while True:
    print('com : ', computer)
    if me == computer:
        attacker = ''
        print('------------------------------------')
        computer = random.choice(['묵', '찌', '빠'])
        me = input('묵찌빠 중 하나를 입력하세요 : ')
    elif (me == '묵' and computer == '찌') or (me == '찌' and computer == '빠') or (me == '빠' and computer == '묵'):
        attacker = 'me'
        break
    else:
        attacker = 'com'
        break

# 승자가 나올때 까지 반복
print(attacker, '이 공격권을 가지고 있습니다.')
while True:
    print('------------------------------------')
    computer = random.choice(['묵', '찌', '빠'])
    me = input('묵찌빠 중 하나를 입력하세요 : ')
    print('com은', computer, '을 냈습니다.')
    # CASE 1) 비겼을 때 attacker가 이김
    if me == computer and attacker == 'me':
        print('승리하셨습니다! WIN')
        break
    elif me == computer and attacker == 'com':
        print('패배하셨습니다... LOSE')
        break
    # CASE 2) attacker 결정
    if (me == '묵' and computer == '찌') or (me == '찌' and computer == '빠') or (me == '빠' and computer == '묵'):
        attacker = 'me'
    else:
        attacker = 'com'
    print(attacker, '이 공격권을 가지고 있습니다.')