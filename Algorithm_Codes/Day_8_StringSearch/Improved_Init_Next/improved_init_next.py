def improved_init_next(p):
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
            # print(f"값(p[i]:{p[i]} != p[j]:{p[j]}")
            # print(f"재시작 위치: {i + 1}")
        i += 1
        j += 1
    print(next)
    print(f"총 비교횟수 : {comp}")


if __name__ == "__main__":
    pattern_list = [
        # 'AAAAAAAA'
        # 'abababca',
        # '10100111'
        # 'aaaaaaaaa',
        # '00000001',
        # '10100111',
        'ababca',
        # 'abababca',
        # 'abcabcabc',
        # 'abcabcacab',
        # 'abracadabra'
    ]

    for i in range(len(pattern_list)):
        pattern = pattern_list[i]
        print(f"-------------{i + 1} 번째 : {pattern}-------------")
        next = [0] * len(pattern)
        improved_init_next(pattern)
        print('스트링 탐색 종료')