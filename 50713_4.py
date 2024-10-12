import time
out = ""
for i in range(10):
    time.sleep(1)
    out = "Loading"
    for j in range(i):
        out += "."
    print(out)
print("Done!")