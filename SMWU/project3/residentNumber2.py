#2.주민번호 검증하기
#입력 : 주민번호 입력
#출력 : 함수 3개로 주민번호 검증하기

def formatOK(s) :
    if len(s)==14 :
        if s[:6].isdigit() and s[6]=='-' and s[7:].isdigit() :
            s=True
            
            return s
        else :
            s=False
            return s

def frontOK(f) :
    yy=int(f[:2])
    mm=f[2:4]
    dd=int(f[4:6])
    if mm=='01' or mm=='03' or mm=='05' or mm=='07' or mm=='08' or mm=='10' or mm=='12':
        if dd>=1 and dd<=31 :
            f=True
        else:
            f=False
    elif mm=='04'or mm=='06' or mm=='09' or mm=='11':
        if dd>=1 and dd<=30 :
            f=True
        else:
            f=False
    elif mm=='02' :
        if yy>=20:#1900s
            y=yy+1900
            if (y%4==0 and y%100!=0) or (y%400==0) :
                if dd>=1 and dd<=29 :
                    f=True
                else :
                    f=False
            else:
                if dd>=1 and dd<=28 :
                    f=True
                else:
                    f=False
        else:#2000s
            Y=yy+2000
            if (Y%4==0 and Y%100!=0) or (Y%400==0) :
                if dd>=1 and dd<=29 :
                    f=True
                else:
                    f=False
            else:
                if dd>=1 and dd<=28 :
                    f=True
                else:
                    f=False
    else:
        f=False

    return f
        
        

def backOK(b) :
    a=int(b[0])
    B=int(b[1])
    c=int(b[2])
    d=int(b[3])
    e=int(b[4])
    f=int(b[5])
    g=int(b[6])
    h=int(b[7])
    i=int(b[8])
    j=int(b[9])
    k=int(b[10])
    l=int(b[11])
    m=int(b[12])
    M=11-((2*a+3*B+4*c+5*d+6*e+7*f+8*g+9*h+2*i+3*j+4*k+5*l)%11)
    if M==10 :
        if m==0 :
            b=True
        else :
            b=False
    elif M==11 :
        if m==1 :
            b=True
        else :
            b=False
    elif M==m:
        b=True
    else:
        b=False
    return b
    
    
print('=================================================')
print('        1.주민번호 검증하기  2. 종료           ')
print('=================================================')

while True :
    menu = input('메뉴 선택 :')
    while not menu.isdigit() :
        menu=input('메뉴 다시 선택 :')

    if menu =='1' :
        s = input('주민번호를 입력하세요:')
        (p,x,g)=s.partition('-')
        f=str(p)
        b=str(p+g)

        if formatOK(s)==True :
            if frontOK(f)==True :
                if backOK(b)==True:
                    print('검증되었습니다. 올바른 주민번호입니다.')
                else :
                    print('검증번호 오류입니다. 올바른 주민번호가 아닙니다.')
            else :
                print('존재하지 않는 날짜입니다. 올바른 주민번호가 아닙니다.')
        else :
            print('\'-\'을 포함해서 14자리 숫자로 입력하세요.')


    elif menu=='2' :
        print('종료합니다.')
        break
    else :
        print('잘못선택하셨습니다. 다시 선택하세요')
    print('==============================================')

        
