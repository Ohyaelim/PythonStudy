#3.N의 보수 구하기
#입력: 자연수와 베이스 입력
#출력: 입력 값에 대한 N의 보수를 구함


# N의 보수 구하는 함수
def complementN(num, base) :
    if num == 0 :
        return 0
    else :
        inStr = str(num)
        ans = ''
        for c in inStr :
            d = base - int(c)
            ans = ans + str(d)
        return int(ans)

# main part
num = int(input('자연수를 입력하세요: '))
base = int(input('베이스(N)을 입력하세요: '))

print('%d의 %d의 보수는 %d입니다.' %(num, base, complementN(num, base)))
