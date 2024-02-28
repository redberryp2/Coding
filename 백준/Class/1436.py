n = int(input())

same = 666
count= 0
while True:
    if '666' in str(same):
        count +=1

    if count == n:
        print(same)
        break
    same +=1