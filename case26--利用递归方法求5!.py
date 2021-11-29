"""
题目：利用递归方法求5!。

程序分析：递归公式：fn=fn_1*4!
"""
def fn(n):
    if n==1:
        sum=1
    else:
        sum=n*fn(n-1)
    return sum

print(fn(5))
