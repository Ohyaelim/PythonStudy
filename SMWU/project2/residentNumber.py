#2.주민번호 검증하기
#입력: 메뉴 선택, 주민번호 입력
#출력: 주민번호의 검증 규칙에 따른 검증 여부

print('================================================')
print('    1. 주민번호 검증하기    2. 종료             ')
print('================================================')

while True :
    menu = input('메뉴 선택 : ')
    while not menu.isdigit() :
        menu = input('메뉴 선택 : ')
    
    if menu == '1' :
        id_num = input('주민번호를 입력하세요: ')

        if len(id_num)==14 :
            if id_num[:6].isdigit() and id_num[6]=='-' and id_num[7:].isdigit() :
                if id_num[7]=='1' or id_num=='2' :
                    print('검증되었습니다. 올바른 주민번호입니다.')
                else :
                    print('올바르지 않은 주민번호입니다.')
            else :
                print('올바르지 않은 주민번호입니다.')
        
        else :
            print('올바르지 않은 주민번호입니다.')
    elif menu == '2' :
        print('종료합니다.')
        break
    
    else :
        print('잘못선택하셨습니다. 다시 선택하세요')

    print('===========================================================')
