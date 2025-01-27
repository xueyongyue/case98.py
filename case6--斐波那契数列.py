"""
题目：斐波那契数列。

程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
"""
#使用递归
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

#输出第n个斐波那契数列
print(fib(5))