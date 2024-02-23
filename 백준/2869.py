a,b,c = map(int,input().split())
k = (c-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)