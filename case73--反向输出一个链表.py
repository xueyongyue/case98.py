"""
题目：反向输出一个链表。
"""
l=[]
for i in range(3):
    n=int(input("请输入一个数字:\n"))
    l.append(n)
l.reverse()
print(l)