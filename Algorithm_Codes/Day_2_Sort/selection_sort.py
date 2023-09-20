import random, time

def selection_sort(a, n):
    for i in range(1, len(a)):
        min_num = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_num]:
                min_num = j
        a[min_num], a[i] = a[i], a[min_num]

def check_sort(a, n):
    is_sorted = True
    for i in range(1, n):
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
    #     N = 5000 * j
    #     a = []
    #     a.append(None)
    #     for i in range(N):
    #         a.append(random.randint(1, N))
    #     start_time = time.time()
    #     selection_sort(a, N)
    #     end_time = time.time() - start_time
    #     print(f'선택 정렬의 실행 시간 ({j}N = %d) : %0.3f' % (N, end_time))
    #     check_sort(a, N)
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
        selection_sort(a, N)
        end_time = time.time() - start_time
        print(f'선택 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
        check_sort(a, N)
