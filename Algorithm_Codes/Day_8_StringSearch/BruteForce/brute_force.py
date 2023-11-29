def bruteForce(p, t, k):
    M = len(p)
    N = len(t)

    # k는 이전 탐색이 끝난 지점부터 이어주는 역할.
    i, j = k, 0

    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    # pattern 길이와 j(새로 탐색한 pattern 의 끝 index)가 같으면
    if j == M:
        return i - M
    else:
        return i


if __name__ == "__main__":
    text = 'ababababcababababcaabbabababca' + '\0'
    pattern = 'abababca'
    M = len(pattern)
    N = len(text)
    K = 0
    while True:
        pos = bruteForce(pattern, text, K)
        K = pos + M
        if K < N:
            print('패턴이 나타난 위치 : ', pos)
            # print(f"재 시작 위치 (k) : {K}")
        else:
            break
    print('스트링 탐색 종료')
