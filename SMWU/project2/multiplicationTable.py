#1. 구구단을 가로로 출력하기
#출력: 구구단 출력

print('==================== 구구단 출력하기 ========================')
i=0
dan=0
for dan in range(2,10,1):
    print(' ')
    for i in range(1,10,1) :
        print('%dX%d=%d'%(dan,i,dan*i),end=' ')
