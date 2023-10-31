file_name = input()
with open(file_name) as test:
    data = test.read().split()
    words = dict()

    for word in data:
        words.setdefault(word, 0)
        words[word] += 1

    words = list([(number, word) for word, number in words.items()])
    words = sorted(words, key = lambda item: (-item[0], item[1]))

    for (count, word) in words:
        print(count, word)

test.close()