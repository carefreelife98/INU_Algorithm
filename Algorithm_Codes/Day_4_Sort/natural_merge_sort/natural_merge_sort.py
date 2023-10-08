import random
import time

def merge_from_sorted(l1, l2):
    i1 = 0
    i2 = 0
    len_l1 = len(l1)
    len_l2 = len(l2)

    merged = []
    while i1 < len_l1 or i2 < len_l2:
        if i1 >= len_l1 or i2 >= len_l2:
            merged += l1[i1:] + l2[i2:]
            break

        if l1[i1] <= l2[i2]:
            merged.append(l1[i1])
            i1 += 1
        else:
            merged.append(l2[i2])
            i2 += 1
    return merged


def generate_runs(l):
    if len(l) <= 1:
        return l
    len_l = len(l)

    prev_item = l[0]
    runs = []
    run = [prev_item]

    i = 1
    while i < len_l:
        if prev_item > l[i]:
            runs.append(run)
            run = [l[i]]
        else:
            run.append(l[i])

        prev_item = l[i]
        i += 1

    runs.append(run)  # add last run
    return runs


def natural_merge_sort(runs):
    len_runs = len(runs)

    if len_runs <= 1:
        return runs

    while len_runs > 1:
        rst = []
        for i in range(0, len_runs, 2):
            if i == len_runs - 1:
                rst.append(runs[i])
            else:
                rst.append(merge_from_sorted(runs[i], runs[i + 1]))
        # print(f'합병된 Runs: {rst}')
        runs = rst
        len_runs = len(runs)

    return rst[0]

def merge(a, l, m, r):
    i = l
    j = m+1
    k = l

    # 배열 b는 함수 외부에서“b = a.copy()” 명령문을 사용하여 주어진다고 가정
    b = a.copy()
    # a[i]와 a[j]를 비교하여 작은 값을 b[k]에 저장
    while i <= m and j <= r:
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
        k += 1
    while i <= m:
        b[k] = a[i]
        i += 1
        k += 1
    while j <= r:
        b[k] = a[j]
        j += 1
        k += 1
    for p in range(l, r + 1):
        a[p] = b[p]

def mergeSort(a, l, r):
    if r > l:
        m = (r+l)//2
        mergeSort(a, l, m)
        mergeSort(a, m+1, r)
        merge(a, l, m, r)

if __name__ == "__main__":
    N = 10000
    a = [-1]

    # for i in range(1, N+1):
    #     a.append(random.randint(1, N))
    for i in range(N, 0, -1):
        a.append(i)
    a2 = a.copy()

    print(f"[Natural Merge Sort] 초기 배열 상태 a = {a}")
    start = time.time()
    a = natural_merge_sort(generate_runs(a))
    end = time.time() - start
    print(f"[Natural Merge Sort] 정렬 후 a = {a}")
    print(f'자연 합병 정렬의 실행 시간 (N = %d) : %0.3f\n\n' % (N, end))

    print(f"[Merge Sort] 초기 배열 상태 a2 = {a2}")
    start = time.time()
    mergeSort(a2, 1, N)
    end = time.time() - start
    print(f"[Merge Sort] 정렬 후 a2 = {a2}")
    print(f'합병 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end))