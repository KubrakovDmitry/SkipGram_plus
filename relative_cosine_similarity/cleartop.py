from Word import Word
from outPutExcel import outputExcel

def creatLists(oldList):
    newList = []
    for item in oldList:
        newList.append(item[0])
    return newList


def calculateTop(listCBOW2, listCBOW6, listSG2, listSG6):
    
    f = open('Top-100.txt', 'w')

    setCBOW2 = set(creatLists(listCBOW2))
    setCBOW6 = set(creatLists(listCBOW6))
    setSG2 = set(creatLists(listSG2))
    setSG6 = set(creatLists(listSG6))

    itersectionCBOW = setCBOW2 & setCBOW6
    intersectionSG = setSG2 & setSG6

    dictCBOW = []
    dictSG = []

    auxiliaryCBOW = []
    auxiliarySG = []

    for i in itersectionCBOW:
        val2 = 0
        val6 = 0
        for j in listCBOW2:
            if j[0] == i:
                val2 = j[1]
        for j in listCBOW6:
            if j[0] == i:
                val6 = j[1]
        word = Word(i, abs(val2 - val6), val6)
        word2 = Word(i, round(val2, 4), round(val6, 4))
        #if val6 != 0.0:
        #    word = Word(i, abs(val2 - val6), val6)
        #else:
        #    word = Word(i, abs(val2 - val6), val2)
        auxiliaryCBOW.append(word2)
        dictCBOW.append(word)

    for i in intersectionSG:
        val2 = 0
        val6 = 0
        for j in listSG2:
            if j[0] == i:
                val2 = j[1]
        for j in listSG6:
            if j[0] == i:
                val6 = j[1]
        word = Word(i, abs(val2 - val6), val6)
        word2 = Word(i, round(val2, 4), round(val6, 4))
        #if val6 != 0.0:
        #    word = Word(i, abs(val2 - val6), val6)
        #else:
        #    word = Word(i, abs(val2 - val6), val2)
        dictSG.append(word)
        auxiliarySG.append(word2)
    

    
    dictCBOW.sort(key=lambda x: x.difvalue, reverse=True)
    dictSG.sort(key=lambda x: x.difvalue, reverse=True)
    print('CBOW')
    print('CBOW', file = f)
    print(*dictCBOW, sep = '\n')
    print(*dictCBOW, sep = '\n', file = f)
    print()
    print(file = f)
    print('SG')
    print('SG', file = f)
    print(*dictSG, sep = '\n')
    print(*dictSG, sep = '\n', file = f)

    f.close()

    auxiliaryCBOW.sort(key=lambda x: abs(x.value - x.difvalue), reverse = True)
    auxiliarySG.sort(key=lambda x: abs(x.value - x.difvalue), reverse = True)

    outputExcel(auxiliaryCBOW, 'CBOW')
    outputExcel(auxiliarySG, 'SG')

    f2 = open('auxiliaryFile.txt', 'w')

    print('CBOW')
    print('CBOW', file = f2)
    for i in auxiliaryCBOW:
        print('{0:20}{1:20}{2:20}'.format(i.word, round(i.difvalue, 4), round(i.value, 4)))
        print('{0:20}{1:20}{2:20}'.format(i.word, round(i.difvalue, 4), round(i.value, 4)), file = f2)

    print('')
    print('', file = f2)
    print('SG')
    print('SG', file = f2)
    for i in auxiliarySG:
        print('{0:20}{1:20}{2:20}'.format(i.word, round(i.difvalue, 4), round(i.value, 4)))
        print('{0:20}{1:20}{2:20}'.format(i.word, round(i.difvalue, 4), round(i.value, 4)), file = f2)
    
    f2.close()
    ##print('CBOW, window = 2')
    ##print(*setCBOW2, sep='\n')
    ##print('CBOW, window = 6')
    ##print(*setCBOW6, sep='\n')
    ##print('SG, window = 2')
    ##print(*setSG2, sep='\n')
    ##print('SG, window = 6')
    ##print(*setSG6, sep='\n')
    ##print('intersection of CBOW:')
    ##print(*(setCBOW2 & setCBOW6), sep='\n')
    ##print('intersection of SG:')
    ##print(*(setSG2 & setSG6), sep='\n')

    ##print('CBOW, window = 2', file = f, sep='\n')
    ##print(*setCBOW2, file = f, sep='\n')
    ##print('CBOW, window = 6', file = f, sep='\n')
    ##print(*setCBOW6, file = f, sep='\n')
    ##print('SG, window = 2', file = f, sep='\n')
    ##print(*setSG2, file = f, sep='\n')
    ##print('SG, window = 6', file = f, sep='\n')
    ##print(*setSG6, file = f, sep='\n')
    ##print('intersection of CBOW:', file = f, sep='\n')
    ##print(*(setCBOW2 & setCBOW6), file = f, sep='\n')
    ##print('intersection of SG:', file = f, sep='\n')
    ##print(*(setSG2 & setSG6), file = f, sep='\n')