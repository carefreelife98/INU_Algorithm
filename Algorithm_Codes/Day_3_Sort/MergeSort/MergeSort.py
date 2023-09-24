import random
import sys
import time


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
        print(k, i)
        b[k] = a[i]
        i += 1
        k += 1
    while j <= r:
        print(k, j)
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
    print(f"정렬 후 : {a}")

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

# a.append(i)
if __name__ == "__main__":
    N = 10
    sys.setrecursionlimit(3002)
    a = [-1]
    for i in range(N, 0, -1):
       a.append(random.randint(1, N))
    print(f"초기 배열: {a}")
    start_time = time.time()
    mergeSort(a, 1, N)
    end_time = time.time() - start_time
    print('합병 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
    checkSort(a, N)