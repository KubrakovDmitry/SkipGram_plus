class Differ(object):
    w2 = '-'
    w6 = '-'
    v2 = 0.0
    v6 = 0.0
    dif = 0.0


    def __init__(self, w2, w6, v2, v6):
        self.w2 = w2
        self.w6 = w6
        self.v2 = v2
        self.v6 = v6
        self.dif = self.GetDif()


    def GetDif(self):
        return abs(self.v6 - self.v2)


    def __str__(self):
        return '{0:21} {1:21} \t\t\t {2:21} {3:21} \t\t\t {4:21}'.format(self.w2, self.v2, self.w6, self.v6, self.dif)


