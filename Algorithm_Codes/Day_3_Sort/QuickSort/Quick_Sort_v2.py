import random
import sys
import time
def partition(a, l, r):
    v = a[l]  	# 가장 오른쪽 원소를 피봇으로 정함
    i = l 	# 왼쪽에서 오른쪽으로 움직이는 포인터
    j = r + 1 	# 오른쪽에서 왼쪽으로 움직이는 포인터
    print(f"list = {a} , Pivot = {v}")
    while True:
        while True:
            i += 1
            if not a[i] < v:
                break
        while True:
            j -= 1
            if not a[j] > v:
                break
        if i < j:
            a[i], a[j] = a[j], a[i]
        if not i < j:
            break
    a[l], a[j] = a[j], a[l]
    print(f"루프 종료: {a}")
    return j

def quickSort(a, l, r):
    if r > l:
        i = partition(a, l, r)
        quickSort(a, l, i-1)
        quickSort(a, i+1, r)

def checkSort(a, n):
    is_sorted = True
    for i in range(0, n - 1):
        if a[i] > a[i + 1]:
            is_sorted = False
        if not is_sorted:
            break
    if is_sorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")


if __name__ == "__main__":
    # for j in range(1, 4):
        N = 10
        a = []
        sys.setrecursionlimit(3002)
        for i in range(N):
            a.append(random.randint(1, N))
        print(f"초기 list: {a}")
        # if j == 1:
        #     print("초기 데이터 랜덤 상태")
        # elif j == 2:
        #     a.sort()
        #     print("\n초기 데이터 정렬 완료")
        # else:
        #     a.sort(reverse=True)
        #     print("\n초기 데이터 역순 정렬 완료")
        start_time = time.time()
        quickSort(a, 0, N - 1)
        end_time = time.time() - start_time
        print(f'퀵 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
        checkSort(a, N)
