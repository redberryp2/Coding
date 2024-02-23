a,b = map(int,input().split())

if b >= 45:
    print(a,b-45)
else:
    a= a-1
    if a < 0:
        a= a+24
    b=b+60-45
    print(a,b)