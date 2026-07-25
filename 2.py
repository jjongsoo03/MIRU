students= ['김종수', '김철수','김민수']
grade=[2,2,4]
print(students[1])
print(len(students)) #len 함수 안에 문자열이 들어가는 경우에는 문자열의 길이를 나타내지만 ,list가 들어가면 list의 갯수를 산출함.
print(min(grade))
print(max(grade))
print(min(students)) #그럼 문자열의 최대 최소? 문자의 코드값 기준으로 산출
import statistics
a=statistics.mean(grade)
print(int(a))

a=5
print(a) #한줄씩 처리하는 파이썬, 위의 변수 a와, 아래의 변수 a는 한줄씩 처리됨
#python-documetations-3.x resources: 파이썬 사용 설명서
#혹은 구글 서칭..!
#디버깅 잡아내는 방법
#print함수를 활용해서, 제대로 원하는 값을 출력하고 있는지, 만약 그게 원하는 값이 아니라면, 어디서 값이 튀었는지..
#debugger-한줄한줄 데이터의 변화를 파악할 수 있음, 소스코드가 어떻게 작동하는지 나타냄.
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
a = 2
h = 9
i = 8
j = 7
k = 6
l = 5
m = 4
n = 3
o = 2
p = 1
print(a)

#생활코딩


