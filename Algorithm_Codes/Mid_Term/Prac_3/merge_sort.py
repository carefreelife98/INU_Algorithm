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

N = 10
a = [None, 6, 2, 8, 1, 3, 9, 4, 5, 10, 7]
b = a.copy()
mergeSort(a, 1, N)
print(a)
