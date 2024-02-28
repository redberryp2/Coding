# if i > i-1 [i-(i-1)] append
# i-1>i  and i< i+1 => end.append(i)
# end는 각 분기점의 인덱스, end 값을 기준으로 나눠 다 더하고
#그중 최대값..
# i = i-1 => end 값 없앰//
import sys

n=int(sys.stdin.readline())
hills=list(map(int,sys.stdin.readline().split()))
result=[]
start=[]
end=[]

for i in range(1,len(hills)):
    if hills[i] > hills[i-1]:
        result.append(hills[i]-hills[i-1])
        end += i
    if hills[i] <= hills[i-1]:
        start += i