a='pithonon'
print(a[0]+'y'+a[2:])
number = 3
print("I eat %10d apples." % number)
print('%10.4f' %8.365345) # 소수점 네 번째 자리까지만 표시하고 전체 길이가 10개인 문자열 공간에서 오른쪽으로 정렬하는 예를 보여 준다.
name='김종수'
living='sejong'
print(f'안녕하세요 {living}에 거주중인 {name}이라고 합니다.')
print(f'제 이름의 성은 {name[0]}입니다')

a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0][0])