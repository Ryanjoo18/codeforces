s = list(map(int,input().split("+")))
s.sort()
new = ''
s = list(map(str,s))
l = len(s)
for i in range(l):
    new += s[i]
    if i != l-1:
        new += '+'
print(new)
