import gensim

path1 = 'D:\MAI\Program practices\Python_Practice\PythonApplication34\w2v.model'
path2 = 'D:\MAI\Program practices\Python_Practice\PythonApplication36\w2v.model'
path3 = 'D:\MAI\Program practices\Python_Practice\PythonApplication38\w2v.model'
path4 = 'D:\MAI\Program practices\Python_Practice\PythonApplication40\w2v.model'
path5 = 'D:\MAI\Program practices\Python_Practice\PythonApplication41\w2v.model'
path6 = 'D:\MAI\Program practices\Python_Practice\PythonApplication42\w2v.model'

model1 = gensim.models.Word2Vec.load(path1)
model2 = gensim.models.Word2Vec.load(path2)
model3 = gensim.models.Word2Vec.load(path3)
model4 = gensim.models.Word2Vec.load(path4)
model5 = gensim.models.Word2Vec.load(path5)
model6 = gensim.models.Word2Vec.load(path6)

print()
print('model1: not sg, window = 2')
print(*model1.wv.most_similar(['сушки']), sep='\n')
print()
print('model2: not sg, window = 5')
print(*model2.wv.most_similar(['сушки']), sep='\n')
print()
print('model3: not sg, window = 10')
print(*model3.wv.most_similar(['сушки']), sep='\n')
print()
print('model4: sg = 1, window = 10')
print(*model4.wv.most_similar(['баранки']), sep='\n')
print()
print('model5: sg = 1, window = 2')
print(*model5.wv.most_similar(['баранки']), sep='\n')
print()
print('model6: sg = 1, window = 5')
print(*model6.wv.most_similar(['баранки']), sep='\n')

