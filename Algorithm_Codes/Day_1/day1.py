import random

# 에라토스테네스의 채
def eratos(a, n):
    a[1] = 0
    for i in range(2, n+1):
        if not i < n/2:
            return a
        j = 2
        while i * j <= n:
            a[i*j] = 0
            j = j+1
#
# N = int(input('N = '))
# while N < 1:
#     print(N, '은(는) 자연수가 아닙니다.')
#     N = int(input('N = '))
# A = list(range(N+1))
# res = eratos(A, N)
# for i in range(N+1):
#     if res[i]:
#         print(i, end=' ')


# 두 수의 합
def two_sum(a, n, t):
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if a[i] + a[j] == t:
                print(f"{a[i]} 번째와 {a[j]}번째 원소")
            j += 1
        i += 1

# N = int(input('리스트의 원소 개수 : '))
# A = []
# for x in range(N):
#     A.append(random.randint(1, N * 2))
# print('리스트 : ', A)
# T = int(input('목표값 입력 : '))
# print('두 수의 합이 %d인 원소 쌍' % T)
# two_sum(A, N, T)

def pascal_triangle(h):
    res = []
    pre = [1]
    res.append(pre)
    i = 1
    while i < h:
        cur = [1]
        j = 0
        while j < len(pre) - 1:
            temp = pre[j] + pre[j + 1]
            cur.append(temp)
            j += 1
        cur.append(1)
        res.append(cur)
        pre = cur
        i += 1
    return res
# H = int(input('높이 입력 : '))
# result = pascal_triangle(H)
# for i in range(len(result)):
#     for j in range(len(result[i])):
#         print(result[i][j], end=' ')
#     print()

def longest_sequence(a, s, n):
    max_len = 1
    i = 0
    while i < n:
        left = a[i] - 1
        right = a[i] + 1
        count = 1
        while left in s:
            count += 1
            s.discard(left)
            left -= 1
        while right in s:
            count += 1
            s.discard(right)
            right += 1
        max_len = max(max_len, count)
        i += 1
    return max_len


# N = int(input('난수의 개수 : '))
# while N < 1:
#     print('난수의 개수는 자연수여야 합니다.')
#     N = int(input('난수의 개수 : '))
# A = []
# for i in range(N):
#     A.append(random.randint(1, N))
# print('리스트 : ', A)
# S = set(A)
# print('집합 : ', S)
# print('최장 연속 순차의 길이 : ', longestSequence(A, S, N))

if __name__ == "__main__":
    N = int(input('난수의 개수 : '))
    while N < 1:
        print('난수의 개수는 자연수여야 합니다.')
        N = int(input('난수의 개수 : '))
    A = []
    for i in range(N):
        A.append(random.randint(1, N))
    print('리스트 : ', A)
    S = set(A)
    print('집합 : ', S)
    print('최장 연속 순차의 길이 : ', longest_sequence(A, S, N))