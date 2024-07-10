# 단순 선택 정렬

from typing import MutableSequence

def selection_sort(a: MutableSequence) -> None:
    # 단순 선택 정렬
    n = len(a)
    for i in range(n-1):
        # 정렬할 부분에서 가장 작은 원소의 인덱스
        min = i 
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j
        # 정렬할 부분에서 맨 앞의 원소와 가장 작은 원소를 교환
        a[i], a[min] = a[min], a[i]
    
    for i in a :
        print(i)

a=[3, 1, 5, 9, 6]

selection_sort(a)
