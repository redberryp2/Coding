import sys

n=int(sys.stdin.readline())
boxes=list(map(int,sys.stdin.readline().split()))

boxes.sort()
print(boxes)

