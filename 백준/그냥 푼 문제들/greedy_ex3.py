import sys

n ,m=map(int,sys.stdin.readline().split())
card=[list(map(int,sys.stdin.readline().split())) for i in range(n)]
for i in range(n):
    card[i].sort()
print(card)
result=[]
for j in range(n):
    result.append(card[j][0])

print(max(result))
# for j in range(n):
#     card.sort()