n, m = map(int,input().split())

card_num=list(map(int,input().split()))
result=0

for i in range(n):
    for j in range(1+i,n):
        for k in range(1+j,n):
            if card_num[i] + card_num[j] + card_num[k] > m:
                continue
            else:
                result = max(result,card_num[i]+card_num[j]+card_num[k])

print(result)