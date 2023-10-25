def merge(r1, r2):
    i, j, n1, n2 = 0, 0, len(r1), len(r2)
    b = []
    while i < n1 and j < n2:
        if r1[i] < r2[j]:
            b.append(r1[i])
            i += 1
        else:
            b.append(r2[j])
            j += 1
    if i == n1:
        for k in range(j, n2):
            b.append(r2[k])
    else:
        for k in range(i, n1):
            b.append(r1[k])
    return b

def makeRun(a, n):
    i = 1
    r = []
    while i <= n:
        t = []
        t.append(a[i])
        while i+1 < n and a[i] <= a[i+1]:
            t.append(a[i+1])
            i += 1
        r.append(t)
        i += 1
    return r

def naturalMerge(a, n):
    r = makeRun(a, n)
    print(r)
    m = len(r)
    while m > 1:
        i = 0
        p = []
        while i < m:
            if i == m-1:
                p.append(r[i])
            else:
                p.append(merge(r[i], r[i+1]))
            i += 2
        r = []
        m = len(p)
        for j in range(m):
            r.append(p[j])
    for i in range(n):
        a[i+1] = r[0][i]
    return a


a = [None, 6, 7, 8, 3, 4, 1, 5, 9, 10, 2]
print(naturalMerge(a, 10))
