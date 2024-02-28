n, m = map(int, input().split())

def josephus(n , m):
    result= []
    re_list=[1] * n
    i=-1
    for _ in range(n-1):
        count = 0
        while count < m:
            i = (i + 1) % n
            if re_list[i]:
                count+=1
        re_list[i] = 0
        result.append(i+1)
    result.append(re_list.index(1)+1)
    return result

print('<',end='')
print(*josephus(n,m),end='',sep=', ')
print('>')


