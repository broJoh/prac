from random import randint
        

def baseball():
    strike = 0
    ball = 0
    while strike < 3:

        player = input('숫자를 입력해주세요 : ')
        pl_num = list(map(int, str(player)))
        comp = [randint(0,9), randint(0,9), randint(0,9)]
        # comp = [1, 2, 3]
        strike = 0
        ball = 0


        for i in range(3):
            if pl_num[i] == comp[i]:
                strike += 1
            else:
                if pl_num[i] in comp:
                    ball += 1


        print('%d 스트라이크 %d 볼' % (strike, ball))

    else: 
        print('세개의 숫자를 모두 맞추셨습니다! 게임종료')
        print('게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요')
        num = int(input())
        if num == 1:
            baseball()
        elif num == 2:
            print('종료합니다')
       

baseball()

