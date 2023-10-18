import random
import time
import cocktail_shaker_prof_sourcecode
def cocktail_shaker_sort(a, n):
    # print("\n------------------Cocktail Shaker Sort 시작------------------")

    toggle = False
    # 총 패스 횟수
    for i in range(1, n):
        toggle = not toggle
        match toggle:
            case True:
                for j in range(i - i // 2, n):
                    if a[j] > a[j + 1]:
                        a[j], a[j + 1] = a[j + 1], a[j]
                # print(f"BubbleSort[{i}] : {a}")
            case False:
                for j in range(n - i // 2, 0, -1):
                    if a[j] < a[j - 1]:
                        a[j - 1], a[j] = a[j], a[j - 1]
                # print(f"Reverse BubbleSort[{i}] : {a}")

    # print("------------------Cocktail Shaker Sort 끝------------------\n")

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
        return True
    else:
        print("정렬 오류 발생")
        return False

if __name__ == "__main__":
    N = 10000
    a = [-1]
    for i in range(N, 0, -1):
        a.append(random.randint(1, N))
        a2 = a.copy()

        print(f"초기 배열 상태 a = {a}")
        start = time.time()
        cocktail_shaker_prof_sourcecode.cocktailShaker(a, N)
        end = time.time() - start
        print(f"Cocktail Sort 정렬 후 a = {a}")
        checkSort(a, N)
        print(f'칵테일 쉐이커 정렬의 실행 시간 (N = %d) : %0.3f\n\n' % (N, end))

        print(f"초기 배열 상태 a2 = {a2}")
        start = time.time()
        bubble_sort(a2, N)
        end = time.time() - start
        print(f"버블 정렬 후 a2 = {a2}")
        checkSort(a2, N)
        print(f'버블 정렬의 실행 시간 (N = %d) : %0.3f\n\n' % (N, end))