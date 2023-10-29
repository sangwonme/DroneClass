while True:
    n = input()
    import pdb; pdb.set_trace()
    if n == '0':
        break
    else:
        # TODO : for문을 통해서 0자리부터 중간자리까지 대칭되는 지점과 비교
        for i in range(len(n)//2):
        # TODO : 만약 중간에 틀렸으면 no, 끝까지 돌았으면 yes
            import pdb; pdb.set_trace()
            if n[i] != n[len[n]-i-1]:
                print('no')
                break
            else: 
                if i == len(n)//2 - 1:
                    print('yes')