#버블 정렬
#앞에서 부터 두개씩 비교하며 작은게 나오면 자리 체인지를 해 나아가며
#자리 체인지가 일어나지 않을 때 까지 계속 순회

ex_list = [ 0 , 9 , 3 , 8 , 6 , 5 ,2 ,1]

def BubbleSort(data):
    for index in range(len(data)-1):
        swap = False
        for index2 in range(len(data)-1-index):
            if data[index2] > data[index2 + 1]:
                data[index2],data[index2+1] = data[index2+1],data[index2]
                swap = True
        if swap == False:
            break

BubbleSort(ex_list)
print(ex_list)