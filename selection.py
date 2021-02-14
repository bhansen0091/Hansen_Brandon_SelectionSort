
from typing import Mapping


test_list = [8,5,4,7,9,3,6,2,0,1]

def selection_sort(p_list):
    for i in range(int(len(p_list)-1)):
        min_value = i
        for j in range(i+1, len(p_list)):
            if p_list[j] < p_list[min_value]:
                min_value = j
        if min_value != i:
            p_list[min_value], p_list[i] = p_list[i], p_list[min_value]
    return p_list

print(selection_sort(test_list))