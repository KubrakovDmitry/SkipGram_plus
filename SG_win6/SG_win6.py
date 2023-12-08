import gensim
import string
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = open('moshkov_1_1.txt', 'r', encoding='utf-8').read()

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

sentences = [tokenize_ru(sent) for sent in sent_tokenize(text, 'russian')]

print(len(sentences))
print(sentences[200:209])

model = gensim.models.Word2Vec(sentences, size=100, window=6, min_count=10, workers=4, sg = 1)

model.save('./w2v.model')
print('saved')

