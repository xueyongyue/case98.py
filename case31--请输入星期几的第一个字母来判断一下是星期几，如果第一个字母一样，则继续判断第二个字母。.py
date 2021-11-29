"""
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
"""
letter=input("请输入第一个大写字母：")
if letter=="S":
    letter=input("请输入第二个小写字母：")
    if letter=="a":
        print("星期六")
    elif letter=="u":
        print("星期日")
    else:
        print("输入错误,请输入正确的字母")
elif letter=="T":
      letter=input("请输入第二个小写字母：")
      if letter=="u":
          print("星期二")
      elif  letter=="h":
          print("星期四")
      else:
          print("输入错误，请输入正确的字母")
elif letter=="M":
    print("星期一")
elif letter=="W":
    print("星期三")
elif letter=="F":
    print("星期五")
else:
    print("输入错误")