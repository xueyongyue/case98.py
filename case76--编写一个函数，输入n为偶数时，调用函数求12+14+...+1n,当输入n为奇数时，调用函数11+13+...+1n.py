"""
题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,
当输入n为奇数时，调用函数1/1+1/3+...+1/n
"""
n=int(input("请输入一个整数:"))
def sum(n):
    s=0
    if n%2==0:
        m=n//2
        for i in range(1,m+1):
            s+= 1 / (2*i)
        print(s)

    elif  n%2!=0:
        m = n // 2
        for i in range(1,m+1):
            s+=(1/(2*i-1))
        print(s)

sum(n)