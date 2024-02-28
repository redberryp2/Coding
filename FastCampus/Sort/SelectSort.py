#삽입 정렬
#순회하며 최소값을 찾는다

ex_list = [ 0 , 9 , 3 , 8 , 6 , 5 ,2 ,1]


def SelectSort(data):
    for stand in range(len(data)-1):
        lowest = stand
        for index in range(stand+1,len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[lowest],data[stand]  = data[stand], data[lowest]
    return data

list = SelectSort(ex_list)
print(list)

