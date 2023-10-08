import random

import sys, math
input = sys.stdin.readline

def remain_combination(a, n, m):
    # 나머지만 담은 배열.
    rem = [0] * m
    rem[a[0] % m] += 1

    for i in range(1, n):
        a[i] = (a[i-1] + a[i]) % m
        rem[a[i]] += 1

    # 0의 개수 + 나머지가 같은 것들의 조합
    ans = rem[0]
    for i in rem:
        if i >= 2:
            ans += math.comb(i, 2)
    print(ans)


def get_input():
    a = []
    N = int(input("수의 개수 N 입력: "))
    M = int(input("나누어 떨어질 수 M 입력: "))

    for i in range(N + 1):
        a.append(random.randint(0, 1000000000))
    return a, N, M

if __name__ == "__main__":
    # a, N, M = get_input()
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    print(f"배열 = {a}\n N = {N}, M = {M}")
    remain_combination(a, N, M)

# def remain_combination(a, n, m):
#     # 구간 합
#     sum = a[0]
#     # 나머지 저장 배열
#     # remain = []
#     total, select = 0
#     one = 0
#     zero = 0
#     for i in range(1, n + 1):
#         sum += a[i]
#         # remain.append(sum//2)
#         if sum // n == 1:
#             one += 1
#         else:
#             zero += 1
#

