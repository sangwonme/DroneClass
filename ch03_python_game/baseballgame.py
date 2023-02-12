import random

# 제목, 룰 설명
print('''
===========================================
o--o    O   o-o  o--o o--o    O  o    o    
|   |  / \ |     |    |   |  / \ |    |    
O--o  o---o o-o  O-o  O--o  o---o|    |    
|   | |   |    | |    |   | |   ||    |    
o--o  o   oo--o  o--o o--o  o   oO---oO---o
===========================================

* 숫자 야구 게임을 시작합니다.
* 컴퓨터가 세자리 수를 생각합니다. 각 자리수는 모두 다르며 0을 포함하지 않습니다.                                           
* 컴퓨터가 생각한 수를 맞춰보세요!
    * 만약 예측한 수 중 숫자와 자릿수가 모두 일치하면 STRIKE 입니다.
    * 만약 예측한 수 중 숫자는 같은데 자릿수가 다르면 BALL 입니다.                                           
* 예시 ) 421(정답), 123(예측) -> 1 STRIKE 1 BALL

''')

# 무작위 수 생성
answer = random.sample(range(1, 10), 3)

# life
life = 10

while True:
    # print life
    print('♥︎'*life + '♡'*(10-life))
    # 플레이어 입력
    guess = list(map(int, list(input('정답을 예상해보세요 : '))))
    # S, B
    strike = 0
    ball = 0
    for i in range(3):
        if guess[i] == answer[i]:
            strike = strike + 1
        elif guess[i] in answer:
            ball = ball + 1
    print(strike, 'STRIKE', ball, 'BALL')
    # 종료
    if strike == 3:
        print('정답입니다!')
        break
    
    # life
    life = life -1 
    if life == 0:
        print('게임 오버')
        break
