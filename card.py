import random
class Poker():
    def __init__(self):
        card = []
        color = ['♥','♠','♣','♦']
        number = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        for i in number:
            for k in color:
                card.append(k+i)
                
        self.card = card

    def __str__(self):
        return str(self.card)

    def shuffle(self):
        random.shuffle(self.card)

    def hit(self):
        a = self.card[0]
        self.card.remove(a)
        return a
