"""
题目：字符串排序。
"""
if __name__=='__main__':
    a = input("请输入字符串：\n")
    b = input("请输入字符串：\n")
    c = input("请输入字符串：\n")
    print(a,b,c)

    if a>b:a,b=b,a
    if a>c:a,c=c,a
    if b>c:b,c=c,b

    print('排序之后')
    print(a,b,c)