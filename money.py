class person():
    def __init__(self,house,car,money,earth,hp = 100):
        self.house = house;self.car = car;self.money = money;self.earth = earth
        self.total = self.house*1000000+self.car*100000+self.earth*5000+self.money
        person.hp = hp
    def sold(self,thing,amount=1):
        if thing == 'house':
            if self.house>0:
                self.money += 1000000
                self.house -= 1
            else:
                print('你无家可归.')
        if thing == 'car':
            if self.car>0:
                self.money += 100000*amount
                self.car -= 1*amount
            else:
                print('你的车卖光了')

        if thing == 'earth':
            if self.earth>0:
                am = input('请问卖多少亩(5000/亩):')
                try:
                    i = eval(am)
                    if self.earth-i>0:
                        self.money += i*5000
                        self.earth -= i
                    else:
                        print('你剩余土地不够！')
                except:
                    print('输入有误,操作失败')
    def buy(self,thing,amount=1):
        if thing == 'house':
            if self.money-1000000>=0:
                self.money -= 1000000
                self.house += 1
            else:
                print('资金不足.')
        if thing == 'car':
            if self.money-100000>=0:
                self.money -= 100000*amount
                self.car += amount
            else:
                print('资金不足')

        if thing == 'earth':
            if self.earth>0:
                am = input('请问买多少亩(5000/亩):')
                try:
                    i = eval(am)
                    if self.money-i*5000>=0:
                        self.money -= i*5000
                        self.earth += i
                    else:
                        print('资金不够!')
                except:
                    print('输入有误,操作失败')
    def work(self):
        if self.hp>0:
            self.hp -= 15
            self.money += 8000*self.earth/10
        if self.hp<=0:
            print('你死了')

    def __str__(self):
        return '现有资产：房屋*%d,汽车%d,土地*%d,资金*%d元'%(self.house,self.car,self.earth,self.money)
'''person = person(3,5,12000,10000000)
print(person)
for k in ['car','house','earth']:
    person.sold(k,5)
    print(person)
for k in ['car','house','earth']:
    person.buy(k,1)
    print(person)'''
    
        
        
        
                    
