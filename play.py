from money import person
import time
from game_21 import game
import os
print('你是一个富豪，现有房子*3，车*5，土地*1200亩,钱*10000000元')
person = person(3,5,10000000,1200)
time.sleep(1)
print('你陷入赌博的池沼，请选择你的人生.')
old = 25
def period1(old):
    print('这一年你%d岁'%old)
    print('现在你可以1,买房.2,买车.3,买土地.4,赌博')
    for i in range(3):
        k1 = input('请选择(跳过end):')
        if k1 == 'end':
            break
        elif k1 == '1':
            person.buy('house')
            old+=1
        elif k1 == '2':
            person.buy('car')
            old+=1
        elif k1 == '3':
            person.buy('earth')
            old+=1
        elif k1 == '4':
            a = game.run()
            old+=5
            if a[0] == True:
                person.money += a[1]
            else:
                person.money -= a[1]
        else:
            print('指令错误，请重新输入')
        print(person)
        if person.money <= 0:
            print('你成了穷光蛋')
            break
    return old
def period2(old):
    print('这一年你%d岁'%old)
    print('现在你可以选择:1,卖房.2,卖车.3,卖土地.4,打工.')
    k2 = input('请选择: ')
    if k2 == '1':
        person.sold('house')
        old += 1
    elif k2 == '2':
        person.sold('car')
        old += 1
    elif k2 == '3':
        person.sold('earth')
        old += 1
    elif k2 == '4':
        person.work()
        old += 10
    return old
while old<75:
    if person.money>0:
        old = period1(old)
    else:
        old = period2(old)
print('你老了')
print('最终')
print(person)









             
