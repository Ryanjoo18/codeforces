import math
for _ in range(int(input())):
    n, x = map(int,input().split())
    # n is number of Petya's apartment,
    # x apartments on each floor except for 1st floor
    if n > 2:
        print(math.ceil((n-2)/x)+1)
    else:
        print(1)