k, n, w = map(int,input().split())
# k,2k,3k as price; n dollars; w bananas
# k + 2k + ... + wk = k*w*(w+1)/2
total = k*w*(w+1)//2
if total > n:
    print(total - n)
else:
    print(0)
