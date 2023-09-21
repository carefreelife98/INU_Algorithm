import random
import time

# a = 정렬 대상 리스트[]
# l = 피봇 기준 파티션 분할 시 가장 왼쪽을 가리키는 포인터
# r = " 가장 오른쪽을 가리키는 포인터

def partition(a, l, r):
    v = a[r]  	# 가장 오른쪽 원소를 피봇으로 정함
    i = l 	# 왼쪽에서 오른쪽으로 움직이는 포인터
    j = r - 1 	# 오른쪽에서 왼쪽으로 움직이는 포인터
    print(f"list = {a} , i = {a[i]} , j = {a[j]}, Pivot = {v}")
    # i > v && j < v 조건 충족 시까지 포인터 이동
    while i < j:
        print("While 문 1 시작")
        while (a[i] <= v or a[j] >= v) and i < j:
            if a[i] <= v and i <= j:
                i += 1
                print(f"while 문 2 시작 i={i}")
            if a[j] >= v and i <= j:
                j -= 1
                print(f"while 문 3 시작 j={j}")
        if i > j:
            break
        # 교환
        print(f"{a[i]} 와 {a[j]} 를 교환: ")
        a[i], a[j] = a[j], a[i]
        print(a)
    print(f"i={i} > j={j} 엇갈림!")
    a[i], a[r] = a[r], a[i]
    print(f"{a[i]} 와 {a[r]} 교환")
    print(f"Loop 종료: {a}")
    return i

def quickSort(a, l, r):
    if r > l:
        print("Partition 시작")
        i = partition(a, l, r)
        print("좌측 Sort")
        quickSort(a, l, i-1)

        print("우측 Sort")
        quickSort(a, i+1, r)

def checkSort(a, n):
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
    for j in range(1, 4):
        N = 10
        a = [-1]
        l = 1
        for i in range(N):
            a.append(random.randint(1, N))
        # if j == 1:
        #     print("초기 데이터 랜덤 상태")
        # elif j == 2:
        #     a.sort()
        #     print("\n초기 데이터 정렬 완료")
        # else:
        #     a.sort(reverse=True)
        #     print("\n초기 데이터 역순 정렬 완료")
        start_time = time.time()
        quickSort(a, l, len(a) - 1)
        end_time = time.time() - start_time
        print(f'퀵 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
        checkSort(a, N)