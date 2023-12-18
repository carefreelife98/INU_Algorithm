def init_next(p):
    M = len(p)
    next[0] = -1

    i, j, comp = 1, 0, 0
    while i < M:
        if p[i] == p[j]:
            next[i] = next[j]
        else:
            next[i] = j
        while j >= 0 and p[i] != p[j]:
            j = next[j]
            comp += 1
            print(f"값(p[i]:{p[i]} != p[j]:{p[j]}")
            print(f"재시작 위치: {i + 1}")
        i += 1
        j += 1
    print(f"총 비교횟수 : {comp}")

def KMP(p, t, k):
    M = len(p)
    N = len(t)
    i, j = k, 0
    init_next(p)
    while j < M and i < N:
        while j >= 0 and t[i] != p[j]:
            j = next[j]
        i += 1
        j += 1

    if j == M:
        return i - M
    else:
        return i

if __name__ == "__main__":
    next = [0] * 50
    text = 'ababababcababababcaabbabababca' + '\0'
    pattern = 'abababca'
    M = len(pattern)
    N = len(text)
    K = 0
    while True:
        pos = KMP(pattern, text, K)
        K = pos + 1
        if K <= N - M:
            print('패턴이 나타난 위치 : ', pos)
        else:
            break
    print('스트링 탐색 종료')
