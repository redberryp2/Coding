#큰 수의 법칙 내가 푼 문제
import sys
import time

st_time=time.time()

n, m, k=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split()))
result=0

data2=sorted(data, reverse=True)
print(data2)
result += data2[0]*(m-(m // (k+1))) + data2[1] * m // (k+1)
print(data2[0]*(m-(m // k+1)),data2[1] * (m // k+1))

end_time=time.time()

print(result,end_time-st_time)

# 책이 푼 문재
# import sys
# import time
# n, m, k=map(int,sys.stdin.readline().split())
# data=list(map(int,sys.stdin.readline().split()))
# result=0
# st_time=time.time()
# data.sort()
# first= data[n-1]
# second= data[n-2]
#
# while True:
#     for i in range(k):
#         if m==0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -=1
# end_time = time.time()
# print(result,end_time-st_time)

