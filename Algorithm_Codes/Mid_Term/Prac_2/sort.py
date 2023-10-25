def selection_sort(a, n):
    for i in range(1, n):
        minIndex = i
        for j in range(i+1, n+1):
            if a[minIndex] > a[j]: minIndex = j
        a[minIndex], a[i] = a[i], a[minIndex]

def bubble_sort(a, n):
    for i in range(n, 1, -1):
        for j in range(1, i):
            if a[j] > a[j+1]: a[j], a[j+1] = a[j+1], a[j]

def insertion_sort(a, n):
    for i in range(2, n+1):
        v, j = a[i], i
        while a[j-1] > v:
            a[j] = a[j-1]
            j -= 1
        a[j] = v

def shell_sort(a, n):
    h = 1
    while 3 * h + 1 < n:
        h = 3 * h + 1
    while h > 0:
        for i in range(h+1, n+1):
            v, j = a[i], i
            while j > h and a[j-h] > v:
                a[j] = a[j-h]
                j -= h
            a[j] = v
        h = int(h/3)
