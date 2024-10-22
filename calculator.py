def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a // b
def getRemainder(a, b):
    return a % b

ans = 0.0
operation = input("What do you want to do?(+ - * /)")
a = 0
b = 0
try:
    a = int(input("Please enter number A:"))
    b = int(input("Please enter number B:"))
    match operation:
        case "+":
            ans = plus(a, b)
        case "-":
            ans = minus(a, b)
        case "*" | "8":
            ans = times(a, b)
        case "/":
            print("商數:" + str(devide(a, b)))
            print("餘數:" + str(getRemainder(a, b)))
            ans = ""
        case _:
            raise ValueError("Invalid argument")
    print(ans)
except Exception as e:
    print("ERROR")
    print(e)