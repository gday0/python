import pickle

with open('words.txt', 'r') as file:
    words = file.read()
    words = words.split(' ')

    print(words)
    
    for word in words:
        if 'c' in word:
            word.rstrip(',.')
            print(word)
