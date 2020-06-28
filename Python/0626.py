import sys
import math


num = int(sys.stdin.readline())
square_arr = [x**2 for x in range(math.ceil((10**0.5)*100) + 1)]
D = [0 for i in range(num+1)]

D[1] = 1

if num < 2:
    sys.stdout.write("1")
    exit()

D[2] = 2

for i in range(2, num+1):
    x = math.inf
    limit = -1
    for (j, e) in enumerate(square_arr):
        if e == i:
            D[i] = 1
            break
        elif e > i:
            limit = j
            break

    if limit == -1:
        continue
    else:
        for j in range(1, limit):
            y = square_arr[j]
            z = 1 + D[i-y]
            if z < x:
                x = z

        D[i] = x

sys.stdout.write(str(D[num]))
