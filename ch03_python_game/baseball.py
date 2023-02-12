# packages
import random

# Title
print('''
      :::::::::           :::        ::::::::       ::::::::::       :::::::::           :::        :::        :::  
     :+:    :+:        :+: :+:     :+:    :+:      :+:              :+:    :+:        :+: :+:      :+:        :+:   
    +:+    +:+       +:+   +:+    +:+             +:+              +:+    +:+       +:+   +:+     +:+        +:+    
   +#++:++#+       +#++:++#++:   +#++:++#++      +#++:++#         +#++:++#+       +#++:++#++:    +#+        +#+     
  +#+    +#+      +#+     +#+          +#+      +#+              +#+    +#+      +#+     +#+    +#+        +#+      
 #+#    #+#      #+#     #+#   #+#    #+#      #+#              #+#    #+#      #+#     #+#    #+#        #+#       
#########       ###     ###    ########       ##########       #########       ###     ###    ########## ########## 
''')

# Description
print('''
숫자 야구 게임을 시작합니다!
컴퓨터가 임의의 세자리 수를 정합니다.
당신은 세자리 수를 예측해보세요.

만약 자리와 숫자가 모두 일치한다면 STRIKE 입니다.
만약 숫자만 동일하고 자리가 다르다면 BALL 입니다.
''')

# generate answer
answer = random.sample(range(1, 10), 3)
random.shuffle(answer)


# user's turn w/ input
while True:
    guess = list(map(int, list(input('세자리 수를 입력하세요 : '))))
    print(guess)
    strike = 0
    ball = 0
    for i in range(3):
        if guess[i] == answer[i]:
            strike += 1
        elif guess[i] in answer:
            ball += 1
    if strike == 3:
        print('정답입니다!')
        break
    print('{} STRIKE {} BALL.'.format(strike, ball))
    

