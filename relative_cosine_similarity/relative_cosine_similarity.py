import gensim
from Differ import Differ
import cleartop
import Retraininng_of_the_nain_models as adst
import CalculateTime as ct
from os.path import isfile
import os
import OriginalSG
import Skip_gram_Plus

# функция сравнения
def showDif(list2, list6):
    listDif = []
    for i in range(0, len(list2)):
        item2 = list2[i]
        item6 = list6[i]
        differ = Differ(item2[0], item6[0], item2[1], item6[1])
        listDif.append(differ)
    listDif.sort(key=lambda differ: differ.dif)
    return listDif


# вывод в файл для обоих размеров окон
def dualOutputFile(listmodel1, listmodel2, word, objfile, methodName):
    print(word, file = objfile)
    print(methodName, file = objfile)
    print("window = 2", file = objfile)
    print(*listmodel1, sep='\n', file = objfile)
    print(file = objfile)
    print("window = 6", file = objfile)
    print(*listmodel2, sep='\n', file = objfile)
    #objfile.close()

# функция в файл вывода для сравнения
def funcOutDifFile(listmodel1, listmodel2, word, objfile, methodName):
    print(word, file = objfile)
    print(methodName, file = objfile)
    list2 = listmodel1
    list6 = listmodel2
    print('{0:65}{1:63}{2:30}'.format('window = 2:', 'window = 6:', 'разница:'), file = objfile)
    print(*showDif(list2, list6), sep='\n', file=objfile)
    objfile.close()


# функция вывода на экран для обоих размеров окон
def dualOutputScreen(listmodel1, listmodel2, word, methodName):
    print(word)
    print(methodName)
    print("window = 2")
    print(*listmodel1, sep='\n')
    print()
    print("window = 6")
    print(*listmodel2, sep='\n')


# функция вывода на экран вывода для сравнения
def funcOutDifScreen(listmodel1, listmodel2, word, methodName):
    print(word)
    print(methodName)
    list2 = listmodel1
    list6 = listmodel2
    print('{0:65}{1:63}{2:30}'.format('window = 2:', 'window = 6:', 'разница:'))
    print(*showDif(list2, list6), sep='\n')


def CalculateWords(path1, path2, path3, path4, word_input):
    # загрузка моделей
    model1 = gensim.models.Word2Vec.load(path1) # модель CBOW с window = 2
    model2 = gensim.models.Word2Vec.load(path2) # модель SG с window = 2
    model3 = gensim.models.Word2Vec.load(path3) # модель CBOW с window = 6
    model4 = gensim.models.Word2Vec.load(path4) # модель SG с window = 6

    f = open('Tea_and_cofe.txt', 'w')
	#f.close()

    #f = open('Tea_and_cofe.txt', 'a')
    fdifTea_CBOW = open('dif_of_tea_CBOW.txt', 'w')
    fdifTea_SG = open('dif_of_tea_SG.txt', 'w')
    fdifCofe_CBOW = open('dif_of_cofe_CBOW.txt', 'w')
    fdifCofe_SG = open('dif_of_cofe_SG.txt', 'w')

    n = 100                  # значение топа, например, топ-100

    word = word_input        # слово над которым выполнестся вычисление
    # названия моделей
    CBOW = 'CBOW'           
    SG = 'SG'

    # получение списков слов ассоциативных с словом 
    listCBOW2 = model1.wv.similar_by_word(word, topn = n)
    listCBOW6 = model3.wv.similar_by_word(word, topn = n)
    listSG2 = model2.wv.similar_by_word(word, topn = n)
    listSG6 = model4.wv.similar_by_word(word, topn = n)

    # вывод в файл
    funcOutDifFile(listCBOW2, listCBOW6, word, fdifTea_CBOW, CBOW)
    dualOutputFile(listCBOW2, listCBOW6, word, f, CBOW)
    funcOutDifFile(listSG2, listSG6, word, fdifTea_SG, SG)
    dualOutputFile(listSG2, listSG6, word, f, SG)

    # вывод на экран
    funcOutDifScreen(listCBOW2, listCBOW6, word, CBOW)
    dualOutputScreen(listCBOW2, listCBOW6, word, CBOW)
    funcOutDifScreen(listSG2, listSG6, word, SG)
    dualOutputScreen(listSG2, listSG6, word, SG)

    #вывод результатов для сравнения
    cleartop.calculateTop(listCBOW2, listCBOW6, listSG2, listSG6)

   

    f.close()


def main():
    # пути к обученным моделям
    path1 = 'D:\MAI\Program practices\Python_Practice\CalculateTime\oneCBOW2.model'
    path2 = 'D:\MAI\Program practices\Python_Practice\CalculateTime\oneSG2.model'
    path3 = 'D:\MAI\Program practices\Python_Practice\CalculateTime\oneCBOW6.model'
    path4 = 'D:\MAI\Program practices\Python_Practice\CalculateTime\oneSG6.model'
    while True:
        if not os.path.isfile(path1):
            print(path1.split('\\')[-1], 'не существует!')
        else:
            print(path1.split('\\')[-1], 'существует!')

        if not os.path.isfile(path2):
            print(path2.split('\\')[-1], 'не существует!')
        else:
            print(path2.split('\\')[-1], 'существует!')

        if not os.path.isfile(path3):
            print(path3.split('\\')[-1], 'не существует!')
        else:
            print(path3.split('\\')[-1], 'существует!')

        if not os.path.isfile(path4):
            print(path4.split('\\')[-1], 'не существует!')
        else:
            print(path4.split('\\')[-1], 'существует!')

        # меню
        print('Выбирите действие')
        print('1 -', 'обучение моделей')
        print('2 -', 'дообучение моделей')
        print('3 -', 'вычисление слов')
        print('4 -', 'вызвать оригинальный skip-gram')
        print('5 -', 'вызвать skip-gram plus')
        print('6 -', 'завершить работу программы')

        # ввод номера команды
        action = int(input('>'))
        # обучение моделей
        if action == 1:
            ct.training()
        # дообучение
        if action == 2:
        	if os.path.isfile(path1):
        		adst.Adding_styding(path1)
        	if os.path.isfile(path2):
        		adst.Adding_styding(path2)
        	if os.path.isfile(path3):
        		adst.Adding_styding(path3)
        	if os.path.isfile(path4):
        		adst.Adding_styding(path4)

        # вычисление слов
        if action == 3:
            print('Введите слово')
            word = input('>')
            CalculateWords(path1, path2, path3, path4, word)

        # вызов оригинального skip-gram
        if action == 4:
            print('Введите слово')
            word = input('>')
            print('Введите размер топа')
            n = int(input('>'))
            OriginalSG.OSG(word, n)

        # вызов skip-gram plus
        if action == 5:
            print('Введите слово')
            word = input('>')
            print('Введите размер топа')
            n = int(input('>'))
            Skip_gram_Plus.SGP(word, n)

        # завершение работы программы
        if action == 6:
           break
    

main()
