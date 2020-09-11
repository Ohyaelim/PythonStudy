#3.가위, 바위, 보 게임하기
#입력: 가위, 바위, 보 중 하나 입력
#출력: 알파고와 비교하여 이긴지 판정

import random

my_count, alphago_count=0, 0

while (my_count < 2) and (alphago_count < 2) :
    my_choice = input('당신의 선택은 무엇입니까? (1. 가위, 2. 바위, 3. 보) : ')
    
    while not my_choice.isdigit() :
        my_choice = input('당신의 선택은 무엇입니까? (1. 가위, 2. 바위, 3. 보) : ')

    alphago_choice = random.randint(1,3) #1과 3 사이의 정수 발생
    my_choice = int(my_choice)

    if my_choice == 1 :
        if alphago_choice == 2 :
            alphago_count += 1
            print('당신은 가위를 냈습니다. 알파고는 바위를 냈습니다')
            print('알파고가 이겼습니다. %d승 ' %alphago_count)

        elif alphago_choice == 3 :
            my_count += 1
            print('당신은 가위를 냈습니다. 알파고는 보를 냈습니다')
            print('당신이 이겼습니다. %d승 ' %my_count)
        
        else :
            print('당신은 가위를 냈습니다. 알파고는 가위를 냈습니다')
            print('비겼습니다')
    
    elif my_choice == 2 :
        if alphago_choice == 3 :
            alphago_count += 1
            print('당신은 바위를 냈습니다. 알파고는 보를 냈습니다')
            print('알파고가 이겼습니다. %d승 ' %alphago_count)

        elif alphago_choice == 1 :
            my_count += 1
            print('당신은 바위를 냈습니다. 알파고는 가위를 냈습니다')
            print('당신이 이겼습니다. %d승 ' %my_count)

        else :
            print('당신은 바위를 냈습니다. 알파고는 바위를 냈습니다')
            print('비겼습니다')

    elif my_choice == 3 :
        if alphago_choice == 1 :
            alphago_count += 1
            print('당신은 보를 냈습니다. 알파고는 가위를 냈습니다')
            print('알파고가 이겼습니다. %d승 ' %alphago_count)

        elif alphago_choice == 2 :
            my_count += 1
            print('당신은 보를 냈습니다. 알파고는 바위를 냈습니다')
            print('당신이 이겼습니다. %d승 ' %my_count)
        else :
            print('당신은 보를 냈습니다. 알파고는 보를 냈습니다')
            print('비겼습니다')
    
    else :
        print('잘못선택했습니다.')
 
    print('============================================')

if my_count > alphago_count :
    print('당신의 승리입니다.', end=' ')
else :
    print('알파고의 승리입니다.', end=' ')

print('종료합니다.')
