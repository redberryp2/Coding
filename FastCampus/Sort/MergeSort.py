#병합 정렬
#리스트를 2개 단위로 쪼개 정렬
# 다음 4개 단위로 쪼개 정렬 을 반복

def split(data):
    medium = int(len(data)/2)
    left = data[:medium]
    right = data[medium:]

def merge(left,right):
    meged = []
    left_point,right_point = 0,0
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            meged.append(right[right_point])
            right_point += 1
        else:
            meged.append(left[left_point])
            left_point += 1
    while len(left) > left_point:
        meged.append(left[left_point])
        left_point += 1
    while len(right) > right_point:
        meged.append(right[right_point])
        right_point += 1
    return meged
def MergeSplit(data):
    if len(data) <= 1:
        return data
    medium = int(len(data) /2)
    left = MergeSplit(data[:medium])
    right = MergeSplit(data[medium:])
    return merge(left,right)

import random

data_list = random.sample(range(100),10)
print(MergeSplit(data_list))
