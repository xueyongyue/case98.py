"""
题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
"""
li=["x","y","z"]
for a in li:
    for b in li:
        if a!=b:
            for c in li:
                if a!=c and b!=c:
                    if a != "x" and c != "x" and c != "z":
                        print("a的对手是%s,b的对手是%s,c的对手是%s" % (a,b,c))




