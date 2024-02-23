array= [1,3,5,2,4,6,7,8,9]

for i in range(len(array)):
    min_index= i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i],array[min_index] = array[min_index], array[i]

print(array)