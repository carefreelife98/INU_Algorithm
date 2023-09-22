import random
import sys
import time


def merge(a, l, m, r):
    i = l
    j = m+1
    k = l

    # 배열 b는 함수 외부에서“b = a.copy()” 명령문을 사용하여 주어진다고 가정
    # a[i]와 a[j]를 비교하여 작은 값을 b[k]에 저장
    b = a.copy()

    if a[i] > a[j]:
        b[k] = a[j]
    elif a[i] < a[j]:
        b[k] = a[i]
    else:
        b[k], b[k+1] = a[i], a[j]
    for l in range(r + 1):
        a[l] = b[l]

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

N = 10
# a = [-1, 6, 2, 8, 1, 3, 9, 4, 5, 10, 7]
# quickSort(a, 1, N)
# N = 3000
sys.setrecursionlimit(3002)
a = []
a.append(-1)
for i in range(N, 0, -1):
   a.append(random.randint(1, N))
# a.append(i)
print(f"초기 배열: {a}")
start_time = time.time()
mergeSort(a, 1, N)
end_time = time.time() - start_time
print('합병 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
checkSort(a, N)