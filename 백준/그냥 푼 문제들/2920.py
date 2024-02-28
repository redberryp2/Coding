input_list=list(map(int,input().split()))
up=0
down=0
for i in range(len(input_list)-1):
    if input_list[i] < input_list[i+1]:
        up+=1
    if input_list[i] > input_list[i+1]:
        down+=1

if up == 7:
    print("ascending")
elif down == 7:
    print("descending")
else:
    print("mixed")