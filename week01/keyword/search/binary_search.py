# 이분 탐색(이진 검색) 알고리즘
from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    # 시퀀스 a에서 찾을 key와 일치하는 원소를 이진 검색

    # 검색범위 맨 앞 원소의 인덱스
    pl = 0
    # 검색범위 맨 뒤 원소의 인덱스
    pr = len(a) - 1

    while True:
        # 중앙 원소의 인덱스
        pc = (pl + pr) // 2

        if a[pc] == key:
            # 검색 성공
            return pc
        # key값보다 중앙 원소 값이 작으면 검색범위를 뒤쪽 절반으로 좁힘
        elif a[pc] < key:
            pl = pc + 1
        # key값보다 중앙 원소 값이 크면 검색범위를 앞쪽 절반으로 좁힘
        else: pr = pc - 1

        if pl > pr:
            break
    return -1

if __name__ == '__main__':
    num = int(input())
    x = [None] * num
    
    print('배열 데이터를 오름차순으로 입력')
    x[0] = int(input('x[0]: '))

    # 바로 직전에 입력한 원소 값보다 큰값을 입력
    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i-1]:
                break
    
    ky = int(input('검색할 값 입력'))
    idx = bin_search(x, ky)

    if idx == -1:
        print('검색 실패')
    else:
        print(f'검색 값의 인덱스: {idx}')
