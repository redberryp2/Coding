n= input().lower()
word_list=list(set(n))
cnt=[]

for i in word_list:
    count = n.count(i)
    cnt.append(count)


if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[(cnt.index((max(cnt))))].upper())


