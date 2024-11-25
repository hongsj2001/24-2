import random, time
def quickSort(a, l, r):
    if r > l:
        i = partition(a, l, r)
        quickSort(a, l, i-1)
        quickSort(a, i+1, r)

def partition(a, l, r):
    v, i, j = a[r], l-1, r
    while True:
        i += 1
        while a[i] < v:
            i += 1
        j -= 1
        while a[j] > v:
            j -= 1
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
    a[i], a[r] = a[r], a[i]
    return i
def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i+1]):
            isSorted = False
        if (not isSorted):
            break
    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")
'''
N = 10
a = [-1, 6, 2, 8, 1, 3, 1, 5, 5, 10, 7]
print(a)
quickSort(a, 1, N)
checkSort(a, N)
print(a)

'''
def mergeSort(a, l, r):
    if r > l:
        m = (r+l) // 2
        mergeSort(a, l, m)
        mergeSort(a, m+1, r)
        merge(a, l, m, r)

def merge(a, l, m, r):
    i, j, k = l, m+1, l
    while i <= m and j <= r:
        if a[i] < a[j]:
            b[k] = a[i]
            k += 1
            i += 1
        else:
            b[k] = a[j]
            k += 1
            j += 1
    if i > m:
        for p in range(j, r+1):
            b[k] = a[p]
            k += 1
    else:            
        for p in range(i, m+1):
            b[k] = a[p]
            k += 1
    for p in range(l, r+1):
        a[p] = b[p]


def heapify(a, h, m):
    v=a[h]
    j=2*h
    while (j <= m):
        if ((j < m) and (a[j] < a[j+1])):
            j = j+1
        if (v >= a[j]):
            break
        else:
            a[j // 2] = a[j]
        j=2*j
    a[j//2] = v

def heapSort(a, n):
    for i in range(int(n/2), 0, -1):
        heapify(a, i, n)
    for i in range(n-1, 0, -1):
        a[1], a[i+1] = a[i+1], a[1]
        heapify(a, 1, i)


N = 10
a = [-1, 6, 2, 8, 1, 3, 9, 4, 5, 10, 7]
print(a)
b = a.copy()
start_time = time.time()
mergeSort(a, 1, N)
end_time = time.time() - start_time
print('합병 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
checkSort(a, N)
print(a)


