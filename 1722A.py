for _ in range(int(input())):
    n = int(input()) # length of string s
    s = input()
    l = ["T","i","m","u","r"]
    t = 0

    if n == 5:
        t = 1

    for i in l:
        if i not in s:
            t = 0
            break
    
    if t == 1:
        print("YES")
    else:
        print("NO")