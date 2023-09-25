import random, time, sys
def quickSort(a, l, r):
    if r > l:
        i = partition(a, l, r)
        quickSort(a, l, i-1)
        quickSort(a, i+1, r)

def partition(a, l, r):
    v, i, j = a[r], l-1, r
    while True:
        i += 1
        while a[i] < v:
            i += 1
        j -= 1
        while a[j] > v:
            j -= 1
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
    a[i], a[r] = a[r], a[i]
    return i

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if a[i] > a[i+1]:
            isSorted = False
        if isSorted == False:
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
        for i in range(N, 0, -1):
            a.append(random.randint(1, N))
        print(f"퀵 정렬 전 배열: {a}")
        start_time = time.time()
        quickSort(a, 1, N)
        end_time = time.time() - start_time
        print(f"퀵 정렬 후 배열: {a}")
        print(f'퀵 정렬의 실행 시간 ({j}N = %d) : %0.3f' % (N, end_time))
        checkSort(a, N)
#
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
#         print(f'퀵 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
#         checkSort(a, N)



# if __name__ == "__main__":
#     N = 10
#     sys.setrecursionlimit(3002)
#     a = [-1]
#     for i in range(N, 0, -1):
#         a.append(random.randint(1, N))
#     start_time = time.time()
#     quickSort(a, 1, N)
#     end_time = time.time() - start_time
#     print('퀵 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
#     checkSort(a, N)
