# merge_sort로 확인하는 분할정복
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # 분할
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # 정복 (재귀 호출로 각각 정렬)
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # 결합
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_arr = []
    left_idx, right_idx = 0, 0
    
    # 두 리스트를 병합
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            sorted_arr.append(left[left_idx])
            left_idx += 1
        else:
            sorted_arr.append(right[right_idx])
            right_idx += 1
    
    # 남은 요소를 병합
    sorted_arr.extend(left[left_idx:])
    sorted_arr.extend(right[right_idx:])
    
    return sorted_arr

# 예제 사용
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)