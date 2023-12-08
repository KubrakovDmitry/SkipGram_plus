class Word(object):
    word = '-'
    difvalue = 0.0
    value = 0.0


    def __init__(self, word, difvalue, value):
        self.word = word
        self.value = value
        self.difvalue = difvalue

    def __str__(self):
        return '{0:20} {1:20}'.format(self.word, round(self.value, 4))