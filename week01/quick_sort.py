def qsort(a, left, right) :
    pl = left
    pr = right
    pivot = a[(left+right)//2]

    while pl <= pr:
        while a[pl] < pivot : pl += 1
        while a[pr] > pivot : pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)

def quick_sort(a):
    qsort(a, 0, len(a)-1)
    print(arr)

arr = [5, 8, 4, 2, 6, 1, 3, 9, 7]

quick_sort(arr)