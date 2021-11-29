"""
题目：求0—7所能组成的奇数个数。

程序分析：

组成1位数是4个。

组成2位数是7*4个。

组成3位数是7*8*4个。

组成4位数是7*8*8*4个。
"""
sum = 4
s = 4
for j in range(2,4):
    if j == 2:
        s *= 7
        print(s)
    else:
        s *= 8
        print(s)
    sum += s
print ('sum = %d' % sum)