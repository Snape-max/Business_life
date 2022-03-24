from time import sleep
from set import Set
from card import Poker

from random import choice
class game():
    def __init__(self):
        self.init = 0

    def run():
        print('21点游戏')
        sleep(0.5)
        print('游戏开始')
        sleep(0.5)
        op = input('请下赌注(>10000)\n')
        op1 = choice([100,3000,2000,4000,5000,8000,10000,3000000])
        print('庄家下注%d'%op1)
        a = Poker()
        d = Set()
        p = Set()
        a.shuffle()
        dl = []
        pl = []
        ans = True
        while ans:
            if d.score<18:
                d1 = a.hit()
                dl.append(d1)
                d.pole(d1)
            d2 = a.hit()
            pl.append(d2)
            p.pole(d2)
            print('你抽到了['+d2+']')
            d.dot()
            p.dot()
            if d.score>21:
                print('庄家爆,你赢了!')
                return True,op1
                break
            if p.score>21:
                print('你爆牌,你输了!')
                return False,eval(op)
                break 
            mm = input("你的点数是：%d,要继续抽牌吗(y/n)"%p.score)
            if mm == 'y':
                ans = True
            else:
                ans = False
            
        print('游戏结束')
        sleep(0.75)
        print('庄家: '+str(dl))
        print('点数: %d'%d.score)
        sleep(0.75)
        print('玩家: '+str(pl))
        print('点数: %d'%p.score)
        sleep(0.75)
        if d.score <= 21 and p.score <= 21:
            if d.score>p.score:
                print('你输了')
                return False,eval(op)
            else:
                print('你赢了')
                return True,op1
        else:
            pass
        
