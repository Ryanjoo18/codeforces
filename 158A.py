n, k = map(int,input().split())
# n integers, >= kth place
l = list(map(int,input().split()))
if sum(l) == 0:
    print(0)
    exit()

cut_off = l[k-1]
count = 0
for i in l:
    if (i >= cut_off) and (i != 0):
        count += 1
print(count)
