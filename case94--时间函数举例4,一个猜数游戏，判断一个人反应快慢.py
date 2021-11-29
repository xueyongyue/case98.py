"""
题目：时间函数举例4,一个猜数游戏，判断一个人反应快慢。
"""
import time
import random
start=time.time()
while True:
    play=input('play the game(y/n)?')
    if play=='y':
        number=random.randint(0,10)
        guess=int(input('guess a number: '))
        while True:
            if number>guess:
                guess=int(input("guess a bigger number: "))
            elif number<guess:
                guess=int(input("guess a smaller number: "))
            else:
                end=time.time()
                print ("bingo! ")
                print ("%0.2fs猜中"%(end-start))
                break
    else:
        break