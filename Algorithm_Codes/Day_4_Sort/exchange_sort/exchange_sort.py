import random
import time

def exchange_sort(a, n):
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]

def bubble_sort(a, n):
    for i in range(n, 0, -1):
        for j in range(1, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

def selection_sort(a, n):
    for i in range(1, len(a)):
        min_num = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_num]:
                min_num = j
        a[min_num], a[i] = a[i], a[min_num]

if __name__ == "__main__":
    N = 10000
    a = [-1]

    for i in range(1, N+1):
        a.append(random.randint(1, N))

    a2 = a.copy()
    a3 = a.copy()

    print(f"[exchange] 초기 배열 상태 a = {a}")
    start = time.time()
    exchange_sort(a, N)
    end = time.time() - start
    print(f"[exchange] 정렬 후 a = {a}")
    print(f'교환 정렬의 실행 시간 (N = %d) : %0.3f\n\n' % (N, end))

    print(f"[bubble] 초기 배열 상태 a2 = {a2}")
    start = time.time()
    bubble_sort(a2, N)
    end = time.time() - start
    print(f"[bubble] 정렬 후 a2 = {a2}")
    print(f'버블 정렬의 실행 시간 (N = %d) : %0.3f\n\n' % (N, end))

    print(f"[selection] 초기 배열 상태 a3 = {a3}")
    start = time.time()
    selection_sort(a3, N)
    end = time.time() - start
    print(f"[selection] 정렬 후 a3 = {a3}")
    print(f'선택 정렬의 실행 시간 (N = %d) : %0.3f\n\n' % (N, end))


