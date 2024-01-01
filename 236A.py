s = input()
letters = []
for i in range(len(s)):
    if s[i] not in letters:
        letters.append(s[i])

l = len(letters)
if l % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
