
def fibo(num):
    if num <= 1:
        return num
    return fibo(num-1) + fibo(num -2)
def fibo_dp(num):
    cache = [0 for index in range(num+1)]
    cache[0] = 0
    cache[1] = 1

    for index in range(2,num+1):
        cache[index] = cache[index-1] + cache[index-2]
    return cache[num]

import timeit

start_time = timeit.default_timer()
# 실행할 코드
print(fibo_dp(20))
end_time = timeit.default_timer()

elapsed_time_microseconds = (end_time - start_time) * 1e6
print(f"Elapsed Time: {elapsed_time_microseconds:.2f} microseconds")

start_time = timeit.default_timer()
# 실행할 코드
print(fibo(20))
end_time = timeit.default_timer()

elapsed_time_microseconds = (end_time - start_time) * 1e6
print(f"Elapsed Time: {elapsed_time_microseconds:.2f} microseconds")

