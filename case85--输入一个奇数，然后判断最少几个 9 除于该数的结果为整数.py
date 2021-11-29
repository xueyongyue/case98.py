"""
题目：输入一个奇数，然后判断最少几个 9 除以该数的结果为整数。

程序分析：999999 / 13 = 76923
"""
num=1 #9的个数
k=9  #初始的被除数的值
n=1  #做判断使用
sum=9  #被除数的大小
i=int(input("请输入一个奇数："))
if i % 2 == 0:
    print("输入的不是奇数，请输入奇数!!")
else:
    while n!=0:
        if sum % i ==0:
            n=0
        else:
            k*=10
            sum+=k
            num+=1
    print("奇数%d可以被%d，%d个9整除"%(i,sum,num))

    r=sum/i
    print('%d / %d = %d' % (sum,i,r))






