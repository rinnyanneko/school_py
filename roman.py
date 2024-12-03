table = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000, "EOF":-2147483647}
num = input()
roman = [i for i in num] + ["EOF"]
ans = 0
for i in range(0, len(roman) - 1, 1):
    if table[roman[i]] < table[roman[i+1]]:
        ans -= table[roman[i]]
    else:
        ans += table[roman[i]]
print(ans)