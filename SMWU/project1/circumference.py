#반지름 값으로 원의 면적과 원의 둘레 계산 프로그램 작성
#입력 : 반지름 값
#출력 : 원의 면적과 원의 둘레
#작성일 : 2018-03-30
#수정

import math
r=float(input('반지름을 입력해주세요 :'))
print('===================================================')
pi=math.pi
print('반지름이',r,'인 원의 면적은',round(r**2*pi,2),'입니다.')
print('반지름이',r,'인 원의 둘레는',round(2*r*pi,2),'입니다,')
