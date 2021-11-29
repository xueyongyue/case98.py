"""
题目：有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数
"""
if __name__ == '__main__':
    n=int(input("输入n个整数：\n"))
    m=int(input("移动m个位置：\n"))

    def move(array,n,m):
        array_end=array[n-1]
        for i in range(n-1,-1,-1):
            array[i]=array[i-1]
        array[0]=array_end
        m-=1
        if m>0:move(array,n,m)

    l = []
    for i in range(n):
        l.append(int(input("请输入数字：\n")))
    print("原始列表为：", l)

    move(l,n,m)
    print("移动之后:",l)