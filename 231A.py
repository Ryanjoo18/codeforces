count = 0
for _ in range(int(input())):
    l = list(map(int,input().split()))
    if sum(l) >= 2:
        count += 1
print(count)
