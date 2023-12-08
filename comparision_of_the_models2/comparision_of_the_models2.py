import gensim

path1 = 'D:\MAI\Program practices\Python_Practice\PythonApplication27\w2v.model'
path2 = 'D:\MAI\Program practices\Python_Practice\PythonApplication31\w2v.model'
path3 = 'D:\MAI\Program practices\Python_Practice\CBOW_win6\w2v.model'
path4 = 'D:\MAI\Program practices\Python_Practice\SG_win6\w2v.model'
# загрузка моделей
model1 = gensim.models.Word2Vec.load(path1) # модель CBOW с window = 2
model2 = gensim.models.Word2Vec.load(path2) # модель SG с window = 2
model3 = gensim.models.Word2Vec.load(path3) # модель CBOW с window = 6
model4 = gensim.models.Word2Vec.load(path4) # модель SG с window = 6

top = 100

f = open('output.txt','w')
# вычисление на словами "чай" и "кофе"

# создание списков для результатов
# для слов "чай" и "кофе"
TeaCBOW2 = []
TeaCBOW6 = []
TeaSG2 = []
TeaSG6 = []

CofeCBOW2 = []
CofeCBOW6 = []
CofeSG2 = []
CofeSG6 = []

# запись результатов вычисление в список
CofeCBOW2 = model1.wv.most_similar(positive = ['кофе'], topn = top)
CofeCBOW6 = model2.wv.most_similar(positive = ['кофе'], topn = top)
CofeSG2 = model3.wv.most_similar(positive = ['кофе'], topn = top)
CofeSG6 = model4.wv.most_similar(positive = ['кофе'], topn = top)

TeaCBOW2 = model1.wv.most_similar(positive = ['чай'], topn = top)
TeaCBOW6 = model2.wv.most_similar(positive = ['чай'], topn = top)
TeaSG2 = model3.wv.most_similar(positive = ['чай'], topn = top)
TeaSG6 = model4.wv.most_similar(positive = ['чай'], topn = top)

i = 0
while i < top:
    word, cosine_value = CofeCBOW2[i]
    word2, cosine_value2 = CofeCBOW6[i]
    print('{0:<5}{1:<20f}{2:<50}{3:<65f}'.format(word,cosine_value,word2,cosine_value2), file = f)
    i += 1

print('слово: кофе', file = f)
print()
print('CBOW, window = 2', file = f)
print(*model1.wv.most_similar(positive = ['кофе'], topn = 100), file = f, sep='\n')
print(file = f)
print('SG, window = 2', file = f)
print(*model2.wv.most_similar(positive = ['кофе'], topn = 100), file = f, sep='\n')
print(file = f)
print('CBOW, window = 6', file = f)
print(*model3.wv.most_similar(positive = ['кофе'], topn = 100), file = f, sep='\n')
print(file = f)
print('SG, window = 6', file = f)
print(*model4.wv.most_similar(positive = ['кофе'], topn = 100), file = f, sep='\n')
print(file = f)

print('слово: чай', file = f)
print(file = f)
print('CBOW, window = 2', file = f)
print(*model1.wv.most_similar(positive = ['чай'], topn = 100), file = f, sep='\n')
print(file = f)
print('SG, window = 2', file = f)
print(*model2.wv.most_similar(positive = ['чай'], topn = 100), file = f, sep='\n')
print(file = f)
print('CBOW, window = 6', file = f)
print(*model3.wv.most_similar(positive = ['чай'], topn = 100), file = f, sep='\n')
print(file = f)
print('SG, window = 6', file = f)
print(*model4.wv.most_similar(positive = ['чай'], topn = 100), file = f, sep='\n')
