#4. 리스트에서 가장 큰 수 찾는 함수 작성
#입력: X
#출력: 무작위 리스트 출력후 가장 큰수 찾기

def maxVal(myList) :
    myList.sort()
    a=myList[9]
    return a


#메인코
myList=[]
a=0

import random
for i in range(0,10) :
    myList.append(random.randint(0,100))
    
print('리스트 : %s'%myList)

print('가장 큰 수는 %d입니다.'%maxVal(myList))
