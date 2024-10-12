x = float(input("Please input x position:"))
y = float(input("Please input y position:"))
if x > 0 and y > 0:
    print("Quadrant 1")
elif x > 0 and y < 0:
    print("Quadrant 4")
elif x < 0 and y > 0:
    print("Quadrant 2")
elif x < 0 and y < 0:
    print("Quadrant 3")
elif x == 0:
    if y == 0:
        print("Origional dot")
    else:
        print("x-axis")
elif y == 0:
    print("y-axis")