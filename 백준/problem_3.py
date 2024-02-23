import sys


def find_pp(call_list, end):
    result=0
    while True:
        for i in range(end):
            if i == end:
                break
            if call_list[i] in call_list[i+1]:
                result +=1



n=int(sys.stdin.readline()) #test case
for i in range(n):
    p=int(sys.stdin.readline()) #people's number
    call_list=[list(map(int,sys.stdin.readline().split())) for _ in range(p) ]
    start, end =map(int,sys.stdin.readline().split())
    find_pp(call_list,end)
    print(call_list)











# 1 2
# 2 1 3
# 3 2 4
# 4 3