"""
题目：循环输出列表
"""
l=[]
m=int(input("输入字符串的个数:"))
for i in range(m):
    l.append(input("请输入字符串:\n"))
for i in range(m):
    print(l[i],end=' ')