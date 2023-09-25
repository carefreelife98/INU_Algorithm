import random
import time


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

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
    for j in range(1, 4):
        N = 5000 * j
        a = [-1]
        for i in range(N):
            a.append(random.randint(1, N))
        start_time = time.time()
        heapSort(a)
        end_time = time.time() - start_time
        print(f'히프 정렬의 실행 시간 ({j}N = %d) : %0.3f' % (N, end_time))
        checkSort(a, N)

# if __name__ == "__main__":
#     for y in range(1, 4):
#         N = 500
#         sys.setrecursionlimit(3002)
#         a = [-1]
#         for x in range(N, 0, -1):
#             a.append(random.randint(1, N))
#         if y == 1:
#             print(f"초기 데이터 랜덤 상태: {a}")
#         elif y == 2:
#             a.sort()
#             print(f"\n초기 데이터 정렬 완료: {a}")
#         else:
#             a.sort(reverse=True)
#             # "a[0] = -1" 은 제자리에 다시 위치
#             a[0], a[len(a) - 1] = a[len(a) - 1], a[0]
#             print(f"\n초기 데이터 역순 정렬 완료: {a}")
#         start_time = time.time()
#         quickSort(a, 1, N)
#         print(f"정렬 완료: {a}")
#         end_time = time.time() - start_time
#         print(f'히프 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
#         checkSort(a, N)


# if __name__ == "__main__":
#     arr = [12, 11, 13, 5, 6, 7]
#     heapSort(arr)
#     print("Sorted array is:", arr)
