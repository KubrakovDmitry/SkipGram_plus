from datetime import datetime
from datetime import timedelta
import gensim
import string
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os


def tokenize_ru(file_text):
    # токениация
    tokens = word_tokenize(file_text)

    # удаление знаков препинания
    tokens = [i for i in tokens if (i not in string.punctuation)]

    # удаление стоп-слов
    stop_words = stopwords.words('russian')
    stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', '—', '–', 'к', 'на', '...'])
    tokens = [i for i in tokens if (i not in stop_words)]

    # очистка слова
    tokens = [i.replace("«", "").replace("»", "") for i in tokens]

    return tokens


def training():
    path = 'D:\MAI\Program practices\Python_Practice\A sources text file'

    listFiles = os.listdir(path)
    listResult = []
    for i in listFiles:
        listResult.append(path + '\\' + i)

    text = ''
    for i in listResult:
        text += open(i, 'r', encoding='utf-8').read()

    f = open('results.txt', 'w')

    # CBOW
    time1 = datetime.now()
    sentences = [tokenize_ru(sent) for sent in sent_tokenize(text, 'russian')]



    model1 = gensim.models.Word2Vec(sentences, size=100, window=2, min_count=10, workers=4)
    time2 = datetime.now()

    model1.save('./oneCBOW2.model')
    print('saved')


    cutter = time2 - timedelta(days = time1.day, 
                               hours=time1.hour, 
                               minutes=time1.minute, 
                               seconds=time1.second, 
                               microseconds=time1.microsecond 
                               )
    print('oneCBOW2.model')
    print(cutter)
    print()
    print(file = f)
    print('oneCBOW2.model', file = f)
    print(cutter.hour, cutter.minute, cutter.second, cutter.microsecond, file = f)


    time1 = datetime.now()
    sentences = [tokenize_ru(sent) for sent in sent_tokenize(text, 'russian')]



    model2 = gensim.models.Word2Vec(sentences, size=100, window=6, min_count=10, workers=4)
    time2 = datetime.now()

    model2.save('./oneCBOW6.model')
    print('saved')


    cutter = time2 - timedelta(days = time1.day, 
                               hours=time1.hour, 
                               minutes=time1.minute, 
                               seconds=time1.second, 
                               microseconds=time1.microsecond 
                               )
    print('oneCBOW6.model')
    print(cutter)
    print()
    print(file = f)
    print('oneCBOW6.model', file = f)
    print(cutter.hour, cutter.minute, cutter.second, cutter.microsecond, file = f)

    #SG

    time1 = datetime.now()
    sentences = [tokenize_ru(sent) for sent in sent_tokenize(text, 'russian')]


    model3 = gensim.models.Word2Vec(sentences, size=100, window=2, min_count=10, workers=4, sg=1)
    time2 = datetime.now()

    model3.save('./oneSG2.model')
    print('saved')


    cutter = time2 - timedelta(days = time1.day, 
                               hours=time1.hour, 
                               minutes=time1.minute, 
                               seconds=time1.second, 
                               microseconds=time1.microsecond 
                               )
    print('oneSG2.model')
    print(cutter)
    print()
    print(file = f)
    print('oneSG2.model', file = f)
    print(cutter.hour, cutter.minute, cutter.second, cutter.microsecond, file = f)

    time1 = datetime.now()
    sentences = [tokenize_ru(sent) for sent in sent_tokenize(text, 'russian')]



    model4 = gensim.models.Word2Vec(sentences, size=100, window=6, min_count=10, workers=4, sg=1)
    time2 = datetime.now()

    model4.save('./oneSG6.model')
    print('saved')


    cutter = time2 - timedelta(days = time1.day, 
                               hours=time1.hour, 
                               minutes=time1.minute, 
                               seconds=time1.second, 
                               microseconds=time1.microsecond 
                               )
    print('oneSG6.model')
    print(cutter)
    print('oneSG6.model', file = f)
    print(cutter.hour, cutter.minute, cutter.second, cutter.microsecond, file = f)


    f.close()


def main():
    training()


if __name__=="__main__":
	main()