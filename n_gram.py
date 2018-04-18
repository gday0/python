import pickle   # 파이썬 객체를 파일에 저장할 때 pickle 모듈의 dump 사용

with open('words2.txt', 'r') as file:
    text = file.read()
    words = text.split('\n')
    print(words)

    for word in words:
        #print(word)

        for i in range(len(word) // 2):
            if word[i] != word[-1 - i]:
                break
        print(word)
