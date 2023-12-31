def heapify(a, h, m):
    v, j = a[h], 2 * h
    while j <= m:
        if j < m and a[j] < a[j+1]:
            j += 1
        if v >= a[j]:
            break
        else:
            a[j // 2] = a[j]
        j *= 2
    a[j // 2] = v

def heapSort(a, n):
    for i in range(int(n/2), 0, -1):
        heapify(a, i, n)
    for i in range(n-1, 0, -1):
        a[1], a[i+1] = a[i+1], a[1]
        heapify(a, 1, i)

N = 10
a = [None, 6, 2, 8, 1, 3, 9, 4, 5, 10, 7]
heapSort(a, N)
print(a)
