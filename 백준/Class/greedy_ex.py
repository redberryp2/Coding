#동전 문제

n=int(input())
count=0

coin=[500,100,50,10]
for coins in coin:
    count += n // coins
    n %= coins
print(count)


