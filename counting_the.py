paragraph = input()

word = paragraph.split(' ')

num = 0

print(word)
word.strip(',.')    # 왜 바뀌는 게 없지....

print(word)

for i in word:
    if i == 'the':
        print(i)
        num += 1        
        
print(num)
