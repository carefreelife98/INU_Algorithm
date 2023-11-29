def index(c):
    if ord(c) == 32:
        return 0
    else:
        return ord(c) - 64

def RK(p, t, k):
    q = 33554393
    d = 32
    M, N = len(p), len(t)

    d_m = pow(d, M - 1, q)  # d^(M-1) % q 미리 계산

    h1 = 0  # 패턴의 Hash 값
    h2 = 0  # text 의 첫번째 substring 의 hash 값

    # 패턴 및 text 의 첫번째 Substring 의 hash 값 계산
    for i in range(M):
        h1 = (h1 * d + index(p[i])) % q
        h2 = (h2 * d + index(t[i])) % q

    occurrences = []

    while k <= N - M:
        # hash 값이 맞으면 char 단위로 check
        if h1 == h2 and p == t[k : k + M]:
            occurrences.append(k)

        # text 의 다음 substring 탐색을 위해 hash 값 업데이트
        if k + M < N:
            h2 = (h2 - index(t[k]) * d_m) % q
            h2 = (h2 * d + index(t[k + M])) % q

        k += 1

    return occurrences

if __name__ == "__main__":
    q = 33554393
    d = 32
    text = 'VISION QUESTION ONION CAPTION GRADUATION EDUCATION' + '\0'
    pattern = 'ATION'
    M = len(pattern)
    N = len(text)
    K = 0

    occurrences = RK(pattern, text, K)

    if occurrences:
        print(f'패턴이 나타난 위치 : {occurrences}')
    else:
        print('패턴이 존재하지 않습니다.')

    print('스트링 탐색 종료')
