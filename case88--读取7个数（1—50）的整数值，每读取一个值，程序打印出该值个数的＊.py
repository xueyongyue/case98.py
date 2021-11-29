"""
题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
"""
n=1
while n<=7:
    a=int(input("请输入一个数：\n"))
    while a<1 or a>50:
        a=int(input('请输入一个数：\n'))
    print(a*'*')
    n+=1