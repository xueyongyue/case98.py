"""
题目：学习使用按位与 & 。

程序分析：0&0=0; 0&1=0; 1&0=0; 1&1=1。
"""
a = 5
b = a & 3
print ('a & b = %d' % b)
b &= 7
print ('a & b = %d' % b)