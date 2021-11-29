"""
题目：时间函数举例3。
"""
import time
start = time.perf_counter
for i in range(10):
    print(i)
end=time.perf_counter
print (f'different is {end - start:6.3f}')