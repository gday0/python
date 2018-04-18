with open('words.txt', 'r') as file:
    words = str(file.readlines())
    word = words.split(' ')

    for w in word:
        if 'c' in w:
            print(w.strip(',.'))
