import random
import sys
import time

def heapify(a, h, m):
    v = a[h]
    while h * 2 <= m:
        child = h * 2
        if child < m and a[child] < a[child + 1]:
            child += 1
        if v >= a[child]:
            break
        a[h] = a[child]
        h = child
    a[h] = v

def heapSort(a, n):
    for i in range(n // 2, 0, -1):
        heapify(a, i, n)

    for i in range(n, 0, -1):
        a[1], a[i] = a[i], a[1]
        heapify(a, 1, i - 1)
    print(f"정렬 완료 : {a}")

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i+1]):
            isSorted = False
        if (isSorted == False):
            break
    if isSorted:
        print("정렬 완료\n")
        print()
    else:
        print("정렬 오류 발생\n")
        print()

if __name__ == "__main__":
    N = 10
    sys.setrecursionlimit(3002)
    # a = [-1, 6, 2, 8, 1, 3, 9, 4, 5, 10, 7]
    a = [-1]
    for i in range(N, 0, -1):
       a.append(random.randint(1, N))

    print(f"초기 배열: {a}")
    start_time = time.time()
    heapSort(a, N)
    end_time = time.time() - start_time
    print('히프 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
    checkSort(a, N)
