import random
import re

dna = ['A', 'C', 'G', 'T']

def make_rand_dna():
    while True:
        s_length, _p = (input("임의의 DNA 문자열 S의 길이와 비밀 번호로 사용할 부분 문자열의 길이를 입력하세요 (종료: 999) : ")
                        .split(' ', 2))
        s_length = int(s_length)
        _p = int(_p)
        if _p == 999:
            exit(0)
        if 1 <= _p <= s_length <= 1000000:
            break
        print("1 <= p <= len(S) <= 1000000 조건을 충족하는 p를 입력하세요.")
    # rand_dna_length = random.randint(1, s_length)
    rand_dna = ''
    for _ in range(s_length):
        rand_dna_idx = random.randint(0, 3)
        rand_dna += dna[rand_dna_idx]

    print(f"임의의 DNA 문자열 S = {rand_dna}")
    return rand_dna, _p

def input_num(s):
    while True:
        _count = input("A, C, G, T 의 등장 횟수를 공백으로 구분하여 입력하세요: ").split(' ', 4)
        # 정수 리스트 변환
        _count = list(map(int, _count))
        sum = 0
        for i in range(len(_count)):
            if 0 <= _count[i] <= len(s):
                sum += _count[i]
            else:
                print(f"등장 횟수가 잘못 설정 되었습니다. 다시 입력하세요: ")
                break
            if i == len(_count) - 1 and sum <= len(s):
                return _count


# 전체 문자열 s를 p의 길이와 같은 크기의 sliding window 로 찾으며 각 원소의 개수를 비교.
def search(s, p, c):
    usable_case = 0
    for i in range(len(s)):
        elem_count = [0 for i in range(len(c))]
        for window in s[i:i+p]:
            match window:
                case 'A':
                    elem_count[0] += 1
                case 'C':
                    elem_count[1] += 1
                case 'G':
                    elem_count[2] += 1
                case 'T':
                    elem_count[3] += 1

        if elem_count == c:
            print(f"가능한 비밀번호: {s[i:i+p]} / Text의 {i} ~ {i+p} 위치")
            usable_case += 1
    return usable_case

def test_case(test_num):
    if test_num == 1:
        return "CCTGGATTG", 8
    elif test_num == 2:
        return "GATA", 2

if __name__ == "__main__":
    # 자동 문자열 생성
    S, P = make_rand_dna()

    # 테스트 문자열 생성
    # S, P = test_case(2)

    count = input_num(S)
    result = search(S, P, count)
    print(result)