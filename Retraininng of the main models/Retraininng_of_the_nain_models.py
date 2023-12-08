from datetime import datetime
from datetime import timedelta
import gensim
import string
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os


def tokenize_ru(file_text):
	# firstly let's apply nltk tokenization
	tokens = word_tokenize(file_text)

	# let's delete punctuation symbols
	tokens = [i for i in tokens if (i not in string.punctuation)]

	# deleting stop_words
	stop_words = stopwords.words('russian')
	stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', '—', '–', 'к', 'на', '...'])
	tokens = [i for i in tokens if (i not in stop_words)]

	# cleaning words
	tokens = [i.replace("«", "").replace("»", "") for i in tokens]

	return tokens


def Adding_styding(modelPath):
	path = 'D:\MAI\Program practices\Python_Practice\For retraining'
	f = open('results.txt', 'w')
	
	listFiles = os.listdir(path)
	listResult = []
	for i in listFiles:
		listResult.append(path + '\\' + i)
	
	for i in listResult:
		text = open(i, 'r', encoding='utf-8').read()
		# пути к обученным моделям
		#path1 = 'D:\MAI\Program practices\Python_Practice\CalculateTime\oneCBOW2.model'
		#path2 = 'D:\MAI\Program practices\Python_Practice\CalculateTime\oneSG2.model'
		#path3 = 'D:\MAI\Program practices\Python_Practice\CalculateTime\oneCBOW6.model'
		#path4 = 'D:\MAI\Program practices\Python_Practice\CalculateTime\oneSG6.model'

		# загрузка моделей
		model = gensim.models.Word2Vec.load(modelPath) # модель CBOW с window = 2
		#model1 = gensim.models.Word2Vec.load(path1) # модель CBOW с window = 2
		#model2 = gensim.models.Word2Vec.load(path2) # модель SG с window = 2
		#model3 = gensim.models.Word2Vec.load(path3) # модель CBOW с window = 6
		#model4 = gensim.models.Word2Vec.load(path4) # модель SG с window = 6

		# токенизация предложений
		sentences = [tokenize_ru(sent) for sent in sent_tokenize(text, 'russian')]

		# train model part II

		lv = 0

		try:
			#print('Модель oneCBOW2')
			print('Модель готова!')
			model.train(sentences, total_examples=model.corpus_count, epochs=model.iter)
			#print('Модель oneSG2')
			#model2.train(sentences, total_examples=model.corpus_count, epochs=model.iter)
			#print('Модель oneCBOW6')
			#model3.train(sentences, total_examples=model.corpus_count, epochs=model.iter)
			#print('Модель oneSG6')
			#model4.train(sentences, total_examples=model.corpus_count, epochs=model.iter)
		except Exception as e:
			lv = 1
			print('Проблемы с обучение: \n', e)
		finally:
			if lv == 0:
				model.save(modelPath)
				#model2.save(path2)
				#model3.save(path3)
				#model4.save(path4)
				print('Дообучение прошло успешно!')
			else:
				print('Дообучение завершилось неуспешно!')


def main():
	Adding_styding(modelPath)


main()