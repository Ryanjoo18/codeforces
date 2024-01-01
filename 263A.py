for i in range(5):
    l = list(input().split())
    if '1' in l:
        pos_hor = l.index('1')
        pos_ver = i
        print(abs(pos_hor - 2) + abs(pos_ver - 2))
        exit()
