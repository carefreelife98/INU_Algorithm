import random
import time

def bubble_sort(a, n):
    for i in range(n, 0, -1):
        for j in range(1, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                
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
        bubble_sort(a, N)
        end_time = time.time() - start_time
        print(f'버블 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
        checkSort(a, N)
