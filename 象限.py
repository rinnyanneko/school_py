x = float(input("Please input x axis:"))
y = float(input("Please input y axis:"))
if x > 0 and y > 0:
    print("第一象限")
elif x > 0 and y < 0:
    print("第四象限")
elif x < 0 and y > 0:
    print("第二象限")
elif x < 0 and y < 0:
    print("第三象限")
elif x == 0:
    print("X軸")
elif y == 0:
    print("Y軸")
else:
    print("蛤")