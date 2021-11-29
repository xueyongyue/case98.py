"""
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？
第10次反弹多高？
"""
n = int(input("请输入落地次数："))
h = 100
sum = 0
total = 0
if n == 1:
    total = 100
else:
    for i in range(n-1):
        h = h / 2
        sum += h
        total = 100 + sum
print("共经过%s米" % total)
print("第%s次反弹高度为%s" % (n,h/2))

