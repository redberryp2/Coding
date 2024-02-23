from collections import deque
n=int(input())

def pivo(num):
    i=0
    if num == 0:
        return 0
    for j in range(num):
        i=i+j

    return i
result=[]
for _ in range(n):
    OX=input()
    deq=deque(OX)
    stack=[]
    count=0

    while True:

        a1=deq.popleft()
        if a1 == 'O':
            stack.append(a1)
        if a1 == 'X':
            count += pivo(len(stack)+1)
            stack.clear()
        if len(deq) == 0:
            count += pivo(len(stack)+1)
            result.append(count)
            break
for k in range(n):
    print(result[k])






