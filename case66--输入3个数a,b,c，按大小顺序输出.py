"""
题目：输入3个数a,b,c，按大小顺序输出。
"""
if __name__ == '__main__':
    n1 = int(input('n1 = :\n'))
    n2 = int(input('n2 = :\n'))
    n3 = int(input('n3 = :\n'))


    def haha(p1, p2):
        return p2, p1


    if n1 > n2: n1, n2 = haha(n1, n2)
    if n1 > n3: n1, n3 = haha(n1, n3)
    if n2 > n3: n2, n3 = haha(n2, n3)

    print (n1,n2,n3)