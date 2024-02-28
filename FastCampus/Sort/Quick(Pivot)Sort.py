#피봇 정렬
#시간 복잡도 nlogn = 병합 정렬
#피벗이 최소일 경우 n제곱 만큼의 최악의 시간 복잡도를 갖는다
def QuickSort(data):
    if len(data) <= 1:
        return data
    left,right = [],[]

    pivot = data[0]
    for index in range(1,len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else:
            right.append(data[index])
    return QuickSort(left) + [pivot] + QuickSort(right)

import random

data_list = random.sample(range(100),10)

sorted_list =QuickSort(data_list)
print(sorted_list)