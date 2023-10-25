def exchangeSort(a, n):
    for i in range(1, n):
        for j in range(i+1, n+1):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
        print(a)

a = [None, 3, 1, 2, 4, 6, 5]
exchangeSort(a, 6)
