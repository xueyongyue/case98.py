"""
两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵
"""
x=[]
y=[]
s=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(3):
    x.append([])
    for j in range(3):
        x[i].append(int(input("请输入整数:\n")))
print("数组x为%s" % x)

for i in range(3):
    y.append([])
    for j in range(3):
        y[i].append(int(input("请输入整数:\n")))
print("数组y为%s" % y)

for i in range(3):
    for j in range(3):
        s[i][j]=x[i][j]+y[i][j]
print("数组x和y的和为%s" % s)
