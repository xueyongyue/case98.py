"""
题目：两个变量值互换。
"""
# 方法1
# a=input("请输入一个a的值：")
# b=input("请输入一个b的值：")
# a,b=b,a
# print("a的值为：%s"% a)
# print("b的值为%s"% b)

# 方法2
def chang(a,b):
    a,b=b,a
    return (a,b)

print(chang(1,2))