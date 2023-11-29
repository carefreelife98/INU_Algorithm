def index(c):
    if ord(c) == 32:
        return 0
    else:
        return ord(c)-64

def initSkip(p):
    M = len(p)
    for i in range(NUM):
        skip[i] = M
    for i in range(M):
        skip[index(p[i])] = M - i - 1

def BM(p, t, k):
    M = len(p)
    N = len(t) - 1
    initSkip(p)
    i, j = M - 1 + k, M - 1
    while j >= 0:
        while t[i] != p[j]:
            # 패턴 못 찾은 경우
            if i >= N:
                return N
            s = skip[index(t[i])]
            # 패턴 길이 - 나쁜 문자가 패턴에서 가진 인덱스 > skip 값
            if M - j > s:
                # 텍스트의 인덱스 = 텍스트 인덱스 + 패턴 길이 - 나쁜 문자가 패턴에서 가진 인덱스
                i = i + M - j
            else:
                # 텍스트의 인덱스는 skip 값 만큼 증가
                i = i + s
            j = M - 1
        i -= 1
        j -= 1
    return i + 1

if __name__ == "__main__":
    NUM = 27
    skip = [0] * NUM
    text = 'VISION QUESTION ONION CAPTION GRADUATION EDUCATION' + '\0'
    pattern = 'ATION'
    M = len(pattern)
    N = len(text)
    K = 0
    while True:
        # pos = Pattern 이 나타난 위치
        pos = BM(pattern, text, K)
        K = pos + 1
        if K <= N - M:
            print('패턴이 나타난 위치 : ', pos)
        else:
            break
        print('스트링 탐색 종료')

