# 심사문제: 파일명 형식 적용하기. 파일명 숫자 3개.확장자(xxx.xxx)
files = input().split()

# lambda 인수: 결과
# map(함수, 변수)
# 결과값 출력을 위하여 list 객체로 변환
print(list(map(lambda x: '{0:03d}.{1}'.format(int(x.split('.')[0]), str(x.split('.')[1])), files)))
