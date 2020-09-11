#1. 정수 찾기 프로그램
#입력:숫자입력 혹은 종료키입력
#출력: 정수인지 아닌지 판별 하거나 종료시킴

print('=================================================')
print('정수 검증하기 (종료를 위해 \'q\'를 입력하세요)')
print('=================================================')

def isinteger(n) :
    if n[0]=='-' :
        if  n[1:].isdigit() :
            n=True
            return n
        else :
            n=False
            return n
    elif n.isdigit() :
        n=True
        return n
    elif n=='q' :
        n='bye'
        return n
    else :
        n=False
        return n


while True :
    n=input('숫자를 입력하세요 :')
    if isinteger(n)==True :
        print('정수입니다.')
        print('======================================================')
    elif isinteger(n)==False :
        print('정수아닙니다.')
        print('=======================================================')
    elif isinteger(n)=='bye' :
        print('종료합니다.')
        break
    
