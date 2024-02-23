import sys

a,b,c=map(int,sys.stdin.readline().split())
# try:
if b-a> c-b:
    print(b-a-1)
elif b-a< c-b:
    print(c-b-1)
else:
    print(b-a-1)
# except:
#     print(0)
