def index(c):
    if ord(c) == 32:
        return 0
    else:
        return ord(c)-64

# def RK(p, t, k):
#     d_m, h1, h2 = 1, 0, 0
#     M, N = len(p), len(t)
#
#     for i in range(M):
#         d_m = (d * d_m) % q
#
#     for i in range(M):
#         h1 = (h1 * d + index(p[i])) % q
#         h2 = (h2 * d + index(t[i])) % q
#     i = 0
#     while h1 != h2:
#         if i + M >= N:
#             return N
#         h2 = (h2 + d * q - index(t[i]) * d_m) % q
#         h2 = (h2 * d + index(t[i + M])) % q
#         if i > N - M:
#             return N
#         i += 1
#     return i
def RK(p, t, k):
    d_m, h1, h2 = 1, 0, 0
    M, N = len(p), len(t)

    for i in range(M):
        d_m = (d * d_m) % q
    for i in range(M):
        h1 = (h1 * d + index(p[i])) % q

    i = k
    j = 0
    while i < N and j < M:
        h2 = (h2 * d + index(t[i])) % q
        i += 1
        j += 1

    i = k
    while h1 != h2:
        if i >= N - M:
            return N
        h2 = (h2 + d * q - index(t[i]) * d_m) % q
        h2 = (h2 * d + index(t[i + M])) % q
        if i > N - M:
            return N
        i += 1
    return i

if __name__ == "__main__":
    q = 33554393
    d = 32
    text = 'VISION QUESTION ONION CAPTION GRADUATION EDUCATION' + '\0'
    pattern = 'ATION'
    M = len(pattern)
    N = len(text)
    K = 0

    # count = 0
    while True:
        # count += 1
        pos = RK(pattern, text, K)
        K = pos + 1
        print(f"K={K} <= N={N} - M={M}")
        if K <= N - M:
            print('패턴이 나타난 위치 : ', pos)
        else:
            break

    # print(count)
    print('스트링 탐색 종료')
