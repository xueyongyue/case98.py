"""
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。
"""
a=[1,5,9,13,56,77,108]
i=int(input("请输入数字："))
l=len(a)
# 遍历数组，然后让输入数字和数组数字对比，当小于该数字时插入到数组中
for j in range(l-1):
    if i<=a[j]:
        a.insert(j,i)#数组中插入数据，给出坐标和数据
        print(a)
        break
    elif i<a[0]:
        a.insert(0, i)
        print(a)