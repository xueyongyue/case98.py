"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
"""
import string
s=input("请输入一个字符串：\n")
zimu=0
kongge=0
shuzi=0
qita=0
for i in s:
    if i.isalpha():
        zimu+=1
    elif i.isspace():
        kongge+=1
    elif i.isdigit():
        shuzi+=1
    else:
        qita+=1
print("zimu=%d,kongge=%d,shuzi=%d,qita=%d" % (zimu,kongge,shuzi,qita))


