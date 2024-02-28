import copy
from typing import Any,Sequence


def seq_search(a: Sequence, key: int) -> Any:
    i = 0
    while True:
        if len(a) == i:
            return -1
        if a[i] == key:
            return i
        i +=1

def seq_search_for(a:Sequence, key:int) -> Any:
    for i in range(len(a)):
        if a[i] ==key:
            return i

def seq_search_2(seq: Sequence,key:Any) -> int:
    '''
    보초법
    '''
    a = copy.deepcopy(seq)
    a.append(key)

    i=0
    while True:
        if a[i] == key:
            break
        i +=1
    return -1 if i ==len(seq) else i







x=[1,2,3,4,5,6,7]
print(seq_search(x,4))
print(seq_search_for(x,4))