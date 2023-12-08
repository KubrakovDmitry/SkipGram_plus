from datetime import datetime
from datetime import timedelta
import gensim
import string
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os


def tokenize_ru(file_text):
	# токенизация
	tokens = word_tokenize(file_text)

	# удаление знаков препинания
	tokens = [i for i in tokens if (i not in string.punctuation)]

	# удаление стоп-слов
	stop_words = stopwords.words('russian')
	stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', '—', '–', 'к', 'на', '...'])
	tokens = [i for i in tokens if (i not in stop_words)]

	# очиста 
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

		# загрузка моделей
		model = gensim.models.Word2Vec.load(modelPath) 

		# токенизация предложений
		sentences = [tokenize_ru(sent) for sent in sent_tokenize(text, 'russian')]


		lv = 0

		try:
			print('Дообучение модели запущено!')
			model.train(sentences, total_examples=model.corpus_count, epochs=model.iter)
		except Exception as e:
			lv = 1
			print('Проблемы с обучение: \n', e)
		finally:
			if lv == 0:
				model.save(modelPath)
				print('Дообучение прошло успешно!')
			else:
				print('Дообучение завершилось неуспешно!')
	print('Дообучение', modelPath.split('\\')[-1] ,'прошло успешно!')



def main():
	Adding_styding(modelPath)


if __name__=="__main__":
	main()