"""
题目：求100之内的素数。
"""
l=[]
for i in range(1,101):
    if i >1:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            l.append(i)
print(l)


