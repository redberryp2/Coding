#삽입 정렬
#앞에서부터 숫자 선택
#왼쪽으로 순회하며 선택한 수보다 작은게 나오면 그 바론 오른쪽 자라기 내자리
#반복
# 더 마지막 수까지 하면 끝

ex_list = [ 0 , 9 , 3 , 8 , 6 , 5 ,2 ,1]

def InsertSort(data):
    for index in range(len(data)-1):
        for index2 in range(index +1 ,0,-1):
            if data[index2] < data[index2-1]:
                data[index2],data[index2-1]=data[index2-1],data[index2]
            else:
                break

InsertSort(ex_list)
print(ex_list)


