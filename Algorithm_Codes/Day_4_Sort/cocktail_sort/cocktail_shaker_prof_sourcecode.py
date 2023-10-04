def cocktailShaker(a, n):
    d = True
    i, k = 1, n
    while i <= k:
        if d:
            for j in range(i, k):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
            k -= 1
        else:
            for j in range(k, 1, -1):
                if a[j] < a[j-1]:
                    a[j], a[j-1] = a[j-1], a[j]
            i += 1
        d = not d
        # print(a)

a = [None, 6, 5, 4, 3, 2, 1]
cocktailShaker(a, 6)
