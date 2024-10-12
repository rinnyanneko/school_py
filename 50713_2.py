a = b = int(input('請輸入一個正整數：'))
output = ''
while True:
    for i in range(2,(a+1)):
        if i==b:
            break
        if a%i==0:
            output += f'{i}'
            a = int(a/i)
            break
    if a==1 or a==b:
        break
    else:
        output += '*'
if b == a and b!= 1:
    print(f'{b} 是質數')
elif b == 1:
    print(f'{b} 不是質數，也不能質因數分解')
else:
    print(f'{output}')