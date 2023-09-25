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

# if __name__ == "__main__":
#     for j in range(1, 4):
#         N = 5000 * j
#         a = [-1]
#         for i in range(N, 0, -1):
#             a.append(random.randint(1, N))
#         print(f"합병 정렬 전 배열: {a}")
#         start_time = time.time()
#         mergeSort(a, 1, N)
#         end_time = time.time() - start_time
#         print(f"합병 정렬 후 배열: {a}")
#         print(f'합병 정렬의 실행 시간 ({j}N = %d) : %0.3f' % (N, end_time))
#         checkSort(a, N)
#
if __name__ == "__main__":
    for y in range(1, 4):
        N = 5000
        sys.setrecursionlimit(3002)
        a = [-1]
        for x in range(N, 0, -1):
            a.append(random.randint(1, N))
        if y == 1:
            print(f"초기 데이터 랜덤 상태: {a}")
        elif y == 2:
            a.sort()
            print(f"\n초기 데이터 정렬 완료: {a}")
        else:
            a.sort(reverse=True)
            # "a[0] = -1" 은 제자리에 다시 위치
            a[0], a[len(a) - 1] = a[len(a) - 1], a[0]
            print(f"\n초기 데이터 역순 정렬 완료: {a}")
        start_time = time.time()
        mergeSort(a, 1, N)
        print(f"정렬 완료: {a}")
        end_time = time.time() - start_time
        print(f'합병 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
        checkSort(a, N)


# if __name__ == "__main__":
#     N = 10
#     sys.setrecursionlimit(3002)
#     a = [-1]
#     for i in range(N, 0, -1):
#        a.append(random.randint(1, N))
#     print(f"초기 배열: {a}")
#     start_time = time.time()
#     mergeSort(a, 1, N)
#     end_time = time.time() - start_time
#     print(f"정렬 후 배열: {a}")
#     print('합병 정렬의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
#     checkSort(a, N)