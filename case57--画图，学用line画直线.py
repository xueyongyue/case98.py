"""
题目：画图，学用line画直线。
"""
import turtle

def drawline(n):
    t=turtle.Pen()
    t.color(0.3,0.8,0.6)  #设置颜色，在0--1之间
    t.begin_fill()   #开始填充颜色
    for i in range(n): #任意边形
        t.forward(50)
        t.left(360/n)
    t.end_fill()    #结束填充颜色

drawline(10)