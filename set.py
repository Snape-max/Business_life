class Set():
    def __init__(self):
        self.list = []
        self.score = 0

    def pole(self,c):
        self.list.append(c[-1])

    def dot(self):
        self.score = 0
        for i in self.list:
            if i in '0JQK':
                i = 10
            elif i == 'A':
                i = 11
            else:
                i = eval(i)
            self.score = self.score + i
        if self.score > 21:
            self.score = 0
            for i in self.list:
                if i in '0JQK':
                    i = 10
                if i == 'A':
                    i = 1
                else:
                    i = int(i)
                self.score += i
