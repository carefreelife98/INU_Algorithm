import random
import time

def exchange_sort(a, n):
    for i in range(1, n + 2):
        print(f"i = {i}")
        for j in range(i, n):
            if a[j] < a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]

if __name__ == "__main__":
    N = 10
    a = [-1]

    for i in range(N, 0, -1):
        # a.append(random.randint(1, N))
        a.append(i)
    print(f"초기 배열 `상태 a = {a}")
    start = time.time()
    exchange_sort(a, N)
    end = time.time() - start
    print(f"Exchange Sort 정렬 후 a = {a}")
    print(f'교환 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end))
