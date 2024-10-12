print("Please enter a number")
num = input()
while num != 1:
    if num % 2 == 0:
        num /= 2
        print(num)
    else:
        num *= 3
        print(num)