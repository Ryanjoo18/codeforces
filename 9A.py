W, D = map(int,input().split())
m = max(W,D)
win = 6 - m + 1
if win == 1:
    print("1/6")
elif win == 2:
    print("1/3")
elif win == 3:
    print("1/2")
elif win == 4:
    print("2/3")
elif win == 5:
    print("5/6")
elif win == 6:
    print("1/1")