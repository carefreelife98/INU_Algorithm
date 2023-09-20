import random
import time

def insertion_sort(l, n):
    for i in range(1, n + 1):
        key = l[i]
        j = i - 1
        while j >= 0 and key < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key


def checkSort(a, n):
    is_sorted = True
    for i in range(1, n):
        if a[i] > a[i+1]:
            is_sorted = False
        if not is_sorted:
            break
    if is_sorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")


if __name__ == "__main__":
    for j in range(1, 4):
        N = 5000
        a = []
        a.append(-1)
        for i in range(N):
            a.append(random.randint(1, N))
        if j == 1:
            print("초기 데이터 랜덤 상태")
        elif j == 2:
            a.sort()
            print("\n초기 데이터 정렬 완료")
        else:
            a.sort(reverse=True)
            print("\n초기 데이터 역순 정렬 완료")
        start_time = time.time()
        insertion_sort(a, N)
        end_time = time.time() - start_time
        print(f'삽입 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
        checkSort(a, N)
