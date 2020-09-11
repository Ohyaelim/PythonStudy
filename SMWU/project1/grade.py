#총점과 평균을 구하고 학점주기
#입력 : 국어, 영어, 수학점수
#출력 : 총점, 평균, 학점
#작성일 : 2018-03-30

print('3개 과목의 시험점수를 차례로 입력하세요.')
Korean=int(input('국어 :'))
English=int(input('영어 :'))
Mathematics=int(input('수학 :'))
print('=========================================')
print('=\t\t시험점수 결과\t\t=')
print('=========================================')
total=Korean+English+Mathematics
Average=round(total/3,2)
print('* 총점 :', total)
print('* 평균 :',Average)
if Average>=90 :
    print('* 당신의 학점은 A 입니다.')
elif Average>=80 :
    print('* 당신의 학점은 B 입니다.')
elif Average>=70 :
    print('* 당신의 학점은 C 입니다.')
elif Average>=60 :
    print('* 당신의 학점은 D 입니다.')
else :
    print('* 당신의 학점은 E 입니다.')
    

    
