# 소수인지 아닌지 판별하는 함수
# arg : 판별할 수 num을 받는다.
# return : 만약에 num이 소수이면 true를, 소수가 아니면 false를 return 한다.
def isPrimeNum(num):
    # TODO
    if num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
            if i == num-1:
                return True

for i in range(1, 21):
    print('{}는 소수'.format(i), end='')
    if(isPrimeNum(i)):
        print('입니다.')
    else:
        print('가 아닙니다.')

