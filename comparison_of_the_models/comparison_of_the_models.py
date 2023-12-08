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

top = 5 # размер топа

f = open('output.txt','w')
# вычисление на словами "чай" и "кофе"
print('слово: кофе', file = f)
print()
print('CBOW, window = 2', file = f)
print(*model1.wv.most_similar(positive = ['кофе'], topn = top), file = f, sep='\n')
print(file = f)
print('SG, window = 2', file = f)
print(*model2.wv.most_similar(positive = ['кофе'], topn = top), file = f, sep='\n')
print(file = f)
print('CBOW, window = 6', file = f)
print(*model3.wv.most_similar(positive = ['кофе'], topn = top), file = f, sep='\n')
print(file = f)
print('SG, window = 6', file = f)
print(*model4.wv.most_similar(positive = ['кофе'], topn = top), file = f, sep='\n')
print(file = f)
print()
print('слово: чай', file = f)
print()
print(file = f)
print('CBOW, window = 2', file = f)
print(*model1.wv.most_similar(positive = ['чай'], topn = top), file = f, sep='\n')
print(file = f)
print('SG, window = 2', file = f)
print(*model2.wv.most_similar(positive = ['чай'], topn = top), file = f, sep='\n')
print(file = f)
print('CBOW, window = 6', file = f)
print(*model3.wv.most_similar(positive = ['чай'], topn = top), file = f, sep='\n')
print(file = f)
print('SG, window = 6', file = f)
print(*model4.wv.most_similar(positive = ['чай'], topn = top), file = f, sep='\n')




# вычисление на словами "фрукты" и "овощи"
print()
print('слово: овощи', file = f)
print()
print('CBOW, window = 2', file = f)
print(*model1.wv.most_similar(positive = ['овощи'], topn = top), file = f, sep='\n')
print(file = f)
print('SG, window = 2', file = f)
print(*model2.wv.most_similar(positive = ['овощи'], topn = top), file = f, sep='\n')
print(file = f)
print('CBOW, window = 6', file = f)
print(*model3.wv.most_similar(positive = ['овощи'], topn = top), file = f, sep='\n')
print(file = f)
print('SG, window = 6', file = f)
print(*model4.wv.most_similar(positive = ['овощи'], topn = top), file = f, sep='\n')
print(file = f)
print()
print('слово: фрукты', file = f)
print()
print(file = f)
print('CBOW, window = 2', file = f)
print(*model1.wv.most_similar(positive = ['фрукты'], topn = top), file = f, sep='\n')
print(file = f)
print('SG, window = 2', file = f)
print(*model2.wv.most_similar(positive = ['фрукты'], topn = top), file = f, sep='\n')
print(file = f)
print('CBOW, window = 6', file = f)
print(*model3.wv.most_similar(positive = ['фрукты'], topn = top), file = f, sep='\n')
print(file = f)
print('SG, window = 6', file = f)
print(*model4.wv.most_similar(positive = ['фрукты'], topn = top), file = f, sep='\n')




# вычисление на словами "мясо" и "рыба"
print()
print('слово: мясо', file = f)
print()
print('CBOW, window = 2', file = f)
print(*model1.wv.most_similar(positive = ['мясо'], topn = top), file = f, sep='\n')
print(file = f)
print('SG, window = 2', file = f)
print(*model2.wv.most_similar(positive = ['мясо'], topn = top), file = f, sep='\n')
print(file = f)
print('CBOW, window = 6', file = f)
print(*model3.wv.most_similar(positive = ['мясо'], topn = top), file = f, sep='\n')
print(file = f)
print('SG, window = 6', file = f)
print(*model4.wv.most_similar(positive = ['мясо'], topn = top), file = f, sep='\n')
print(file = f)
print()
print('слово: рыба', file = f)
print()
print(file = f)
print('CBOW, window = 2', file = f)
print(*model1.wv.most_similar(positive = ['рыба'], topn = top), file = f, sep='\n')
print(file = f)
print('SG, window = 2', file = f)
print(*model2.wv.most_similar(positive = ['рыба'], topn = top), file = f, sep='\n')
print(file = f)
print('CBOW, window = 6', file = f)
print(*model3.wv.most_similar(positive = ['рыба'], topn = top), file = f, sep='\n')
print(file = f)
print('SG, window = 6', file = f)
print(*model4.wv.most_similar(positive = ['рыба'], topn = top), file = f, sep='\n')




# вычисление на словами "кровать" и "диван"
print()
print('слово: кровать', file = f)
print()
print('CBOW, window = 2', file = f)
print(*model1.wv.most_similar(positive = ['кровать'], topn = top), file = f, sep='\n')
print(file = f)
print('SG, window = 2', file = f)
print(*model2.wv.most_similar(positive = ['кровать'], topn = top), file = f, sep='\n')
print(file = f)
print('CBOW, window = 6', file = f)
print(*model3.wv.most_similar(positive = ['кровать'], topn = top), file = f, sep='\n')
print(file = f)
print('SG, window = 6', file = f)
print(*model4.wv.most_similar(positive = ['кровать'], topn = top), file = f, sep='\n')
print(file = f)
print()
print('слово: диван', file = f)
print(file = f)
print()
print('CBOW, window = 2', file = f)
print(*model1.wv.most_similar(positive = ['диван'], topn = top), file = f, sep='\n')
print(file = f)
print('SG, window = 2', file = f)
print(*model2.wv.most_similar(positive = ['диван'], topn = top), file = f, sep='\n')
print(file = f)
print('CBOW, window = 6', file = f)
print(*model3.wv.most_similar(positive = ['диван'], topn = top), file = f, sep='\n')
print(file = f)
print('SG, window = 6', file = f)
print(*model4.wv.most_similar(positive = ['диван'], topn = top), file = f, sep='\n')


