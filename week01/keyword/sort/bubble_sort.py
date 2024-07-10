# 버블 정렬

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):
        # 패스에서 교환 횟수를 카운트하고
        # 패스에서 교환이 일어나지 않으면 break으로 종료
        exchange = 0 
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                exchange =+ 1
        if exchange == 0:
            break

if __name__ == '__main__':
    num = int(input())
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    bubble_sort(x)

    for n in x:
        print(n)