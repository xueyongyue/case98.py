"""
打印出如下图案（菱形）
   *
  ***
 *****
*******
 *****
  ***
   *
"""
for i in range(1,5):
    print(" "*(4-i),end="")
    print("*"*(2*i-1))

for j in range(1,4):
    print(" "*(j),end="")
    print("*"*(-2*j+7))