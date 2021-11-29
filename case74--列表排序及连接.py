"""
题目：列表排序及连接。

程序分析：排序可使用 sort() 方法，连接可以使用 + 号或 extend() 方法。
"""
l=[]
k=[]
j=[]
for i in  range(3):
    n=int(input("请输入数字n:\n"))
    m= int(input("请输入数字m:\n"))
    l.append(n)
    k.append(m)
    j=k+l
    j.sort()
print(j)