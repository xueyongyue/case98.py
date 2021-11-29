"""
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
"""
i=int(input("请输入一个5为数："))
#万位
a=i//10000
# print(a)
# 千位
b=i//1000%10
# print(b)
# 百位
c=i//100%10
# print(c)
# 十位
d=i//10%10
# print(d)
# 个位
e=i%10
# print(e)
if a==e and b==d:
    print("输入的数字%s是回文数"% i)
else:
    print("输入的数字%s不是回文数"% i)