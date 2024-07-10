# 힙 정렬 알고리즘 구현하기

from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    # 힙정렬

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        # a[left]~a[right]를 힙으로 만들기
        temp = a[left]

        parent = left
        while parent < (right + 1) // 2:
            # 왼쪽 자식
            cl = parent * 2 + 1 
            # 오른쪽 자식
            cr = cl + 1
            child = cr if cr <= right and a[cr] > a [cl] else cl
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)

    # a[i] ~ a[n-1]을 힙으로 만들기
    for i in range((n-1) // 2, -1, -1):
        down_heap(a, i, n-1)

    for i in range(n -1, 0, -1):
        # 최대값이 a[0]와 마지막 원소를 교환
        a[0], a[i] = a[i], a[0]
        # A[0] ~ a[i-1]을 힙으로 만들기 
        down_heap(a, 0, i - 1)

if __name__ == '__main__':
    num = int(input())
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    heap_sort(x)

    for i in x:
        print(i)



