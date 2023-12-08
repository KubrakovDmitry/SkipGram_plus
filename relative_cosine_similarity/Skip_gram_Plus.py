import gensim

# функция суммирования весов слов
def summer(theList):
    sum = 0
    for item in theList:
        sum += item[1]
    return sum

# функция нормализации
def normalization(oldList):
    sum = summer(oldList)
    newList = []
    for item in oldList:
        newTuple = (item[0], item[1] / sum)
        newList.append(newTuple)
    return newList


def TopofTheTop(Top, model, n):
    TOT = []                # единый список
    auxiliary = []          # вспомагательный список
    # проходим по каждому слова в исходном топе
    for item in Top:
        # вычисление близких слов и запоминание топ для топа
        List = model.wv.similar_by_word(item[0], topn = n)
        # проходим по каждому слову топа для топа
        for item2 in List:
            if item2[0] not in auxiliary:   # если слова ещё не было
                auxiliary.append(item2[0])  # отмечаем что он теперь есть
                item2 = list(item2)         
                item2[1] *= item[1]         # уможение веса W2 на W3
                item2 = tuple(item2)
                TOT.append(item2)           # добавление слова в  единый список
            else:                           # если же слово ранее встречалось
                # ищем такое же слов в едином списке 
                for i in TOT:               
                    if item2[0] == i[0]:
                        index = TOT.index(i)# запоминание индекса слова
                        i = list(i)
                        i[1] += item2[1]    # прибавление веса
                        i = tuple(i)
                        TOT.pop(index)      # удаление слова со старым весом
                        TOT.insert(index, i)# запоминание слова  сновым весом
    # нормирование весов слов близких словам из топа слов близких целевому(word)
    TOT = normalization(TOT)
    # сортировка единого списка по убыванию
    TOT.sort(key = lambda x: x[1], reverse = True)
    return TOT



def SGP(Word, N):
    # окрытие файла для записи результатов
    f = open('outputSGP.txt', 'w')
    # путь модели
    path = 'D:\MAI\Program practices\Python_Practice\CalculateTime\oneCBOW6.model'  
    # загрузка молели
    model = gensim.models.Word2Vec.load(path) # модель CBOW с window = 6            
    n = N               # размер топа
    
    word = Word    # слово
    # вычисление близких слова целевому (word)
    firstTop = model.wv.similar_by_word(word, topn = n)
    # вывод данных на экран и в файл
    print('Для слова:', word)
    print('Для слова:', word, file = f)
    print('исходный топ слов близких целевому:')
    print('исходный топ слов близких целевому:', file = f)
    # нормирование весов слов близких целевому (word)
    firstTop = normalization(firstTop)
    print('сумма весов слов близких целевому после нормализации равна', summer(firstTop))
    print('сумма весов слов близких целевому после нормализации равна', summer(firstTop), file = f)
    print(*firstTop, sep='\n')
    print(*firstTop, sep='\n', file = f)
    # вычисление и вывод взаимозаменяемых слов для слов из топа
    print('сумма весов слов близких словам из топа слов близких целевомупосле нормализации равна', summer(TopofTheTop(firstTop, model, n)))
    print('сумма весов слов близких словам из топа слов близких целевомупосле нормализации равна', summer(TopofTheTop(firstTop, model, n)), file = f)
    print(*TopofTheTop(firstTop, model, n), sep="\n")           
    print(*TopofTheTop(firstTop, model, n), sep="\n", file = f)
    print(file = f)
    print()
    f.close()
   

def main():
    # очистка файла для результатов
    f = open('outputSGP.txt', 'w')
    f.close()
    # ввод данных
    print('введите слово')
    firstWord = input('>')
    #print('введите второе слово')
    #secondWord = input('>')
    print('введите количество слов в топе')
    N = int(input('>'))
    print()
    # реализация Skip-gram+
    SGP(firstWord, N)
    #SGP(secondWord, N)


if __name__=="__main__":
	main()