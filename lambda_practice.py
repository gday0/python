# 심사문제: 파일명 형식 적용하기. 파일명 숫자 3개.확장자(xxx.xxx)
files = input().split()

print(list(map(lambda files: '{0:03d}.{1}',
    format(int(files.split('.')[0]), str(files.split('.')[1])))))
