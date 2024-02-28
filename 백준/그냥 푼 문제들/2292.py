n = int(input())
i=1
j=1
while True:
    if n <= i:
        print(j)
        break
    i += 6*j
    j +=1

