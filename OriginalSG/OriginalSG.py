import gensim


def OSG(word, n):
    f = open('outputSG.txt', 'a')
    path = 'D:\MAI\Program practices\Python_Practice\CalculateTime\oneSG6.model'
    model = gensim.models.Word2Vec.load(path)
    wordlist = model.wv.similar_by_word(word, topn = n)
    print('Для слова ', word)
    print('Для слова ', word, file = f)
    print(*wordlist, sep='\n')
    print(*wordlist, sep='\n', file = f)
    f.close()


def main():
    f = open('outputSG.txt', 'w')
    f.close()
    print('Введите слово')
    word = input('>')
    print('Введите число слов топа')
    n = int(input('>'))
    OSG(word, n)


if __name__ == '__main__':
    main()