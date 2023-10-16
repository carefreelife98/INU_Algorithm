# □ 최소값 찾기
#
# [문제]
# N개의 수 A1, A2, ..., AN과 L이 주어진다.
# Di = Ai-L+1 ~ Ai 중의 최소값이라고 할 때, D에 저장된 수를 출력하는 프로그램을 작성하시오. 이때, i ≤ 0 인 Ai는 무시하고 D를 구해야 한다.
#
# [입력]
# - 첫째 줄에 N과 L이 주어진다. (1 ≤ L ≤ N ≤ 5,000,000)
# - 둘째 줄에는 N개의 수 Ai가 주어진다. (-109 ≤ Ai ≤ 109)
#
# [출력]
# 첫째 줄에 Di를 공백으로 구분하여 순서대로 출력한다.
#
import sys


# L // i == 0 인 경우
# 아직 (-) Index 가 존재함. -> L % i 연산 결과 까지의 i 중 최소값 찾기.
#
# L // i > 0 인 경우부터는 Index 가 0부터 맞춰졌으므로 i - L 부터 i 까지의 원소 중 최소값 반환.
def find_minimum(arr, n, l):
    # print(f"목표 배열에서 L({l}) 범위 index에 존재하는 최소값은 다음과 같습니다.")
    rs = []
    for i in range(1, n + 1):
        if l > i:
            temp_arr = arr[:i]
            # print(f"arr[:{i}] = {temp_arr}")
            temp_arr.sort()
            # rs.append(temp_arr[0])
        else:
            temp_arr = arr[i - l:i]
            # print(f"arr[{i-l}:{i}] = {temp_arr}")
            temp_arr.sort()
        rs.append(temp_arr[0])
    output = ' '.join(map(str, rs))
    # print(output)
    sys.stdout.write(output)

if __name__ == "__main__":
    while True:
        # num = input("N, L 을 입력하시오 (1 ≤ L ≤ N ≤ 5,000,000): ").split()
        num = input().split()
        N, L = int(num[0]), int(num[1])
        if 1 <= L <= N <= 5000000:
            break
        # print("조건이 맞지 않습니다. 다시 입력하세요. (1 ≤ L ≤ N ≤ 5,000,000)")
    # N = 12
    # L = 3
    # a = [1, 5, 2, 3, 6, 4, 5, 7, 3, 5, 2, 6]
    # print(f"N = {N} 개의 정수를 입력하세요: ")
    a = input().split()
    for i in range(N):
        a[i] = int(a[i])
    # print(f"a = {a}")
    # for i in range(N):
    #     a.append(int(input()))
    # print(f"초기 Array = {a}")
    find_minimum(a, N, L)