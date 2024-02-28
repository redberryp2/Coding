#바이너리 서치는 많이 연습해서 이제 눈감고도 함
from typing import Sequence


def binary_search(list:Sequence,a:int) -> int:
    list.sort()
    start = 0
    end =len(list)-1
    while start <= end:
        middle = (start + end) // 2
        if list[middle] == a:
            return middle+1
        elif list[middle] > a:
            end = middle -1
        else:
            start = middle + 1


x=[1,2,3,4,5,6,7,8,9]

print(binary_search(x,9))

