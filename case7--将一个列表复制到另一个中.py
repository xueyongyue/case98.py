"""
题目：将一个列表的数据复制到另一个列表中。

程序分析：使用列表[:]。
"""
# 方法1:
b=[]
a=[1,2,3]
l=len(a)
for i in range(l):
    b.append(a[i])
print(b)

# 方法2：
a=[1,2,3]
b=a[:]
print(b)