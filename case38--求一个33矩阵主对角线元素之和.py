"""
题目：求一个3*3矩阵主对角线元素之和。

程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
"""
sum=0
l=[]
for i in range(3):
    l.append([])
    for j in range(3):
        l[i].append(float(input("输入数字：\n")))
        # print(l)

for i in range(3):
    sum +=l[i][i]
print(sum)
