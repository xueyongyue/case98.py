"""
题目：时间函数举例2。
"""
import time
start=time.time()
for i in range(3000):
    print(i)
end=time.time()

print(end-start)#计算程序运行时间
