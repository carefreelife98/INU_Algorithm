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

N = 10
a = [-1, 6, 2, 8, 1, 3, 9, 4, 5, 10, 7]
quickSort(a, 1, N)
print(a)
