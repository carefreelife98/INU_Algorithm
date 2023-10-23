import random
import time


# 수업시간에 사용한 배열을 테스트 케이스로 사용할 것.

class Dict:
    a = []

    def __init__(self):
        self.a = [-1] * M

    # 삽입 알고리즘
    def insert(self, v):
        x = self.hash(v)
        print(f"\ninsert {v} | Hash 값: {x}")
        if self.a[x] == -1:
            self.a[x] = v
            print(f"바로 할당. index:{x} | value:{self.a[x]} ")
        else:
            while self.a[x] != -1:
                print(f"충돌(index{x} 에 {self.a[x]}값 존재). x값 1 증가")
                x += 1
            self.a[x] = v
            print(f"빈 공간 찾음, 현재 위치 {x}에 {self.a[x]}값 할당.")

    # 탐색 알고리즘
    def search(self, v):
        x = self.hash(v)
        while self.a[x] != -1:
            if self.a[x] == v:
                return self.a[x]
            else:
                x += 1
        print(f"키 값: {v} 를 찾지 못했습니다. 종료")
        return -1

    def hash(self, v):
        return v % M


if __name__ == "__main__":
    # N = 10000
    # M = 10391
    # key = []
    # s_key = []
    # for i in range(N):
    #     r = random.randint(1, 3 * N)
    #     key.append(r)
    #     s_key.append(r)
    N = 17
    M = 19
    key = [1, 19, 5, 1, 18, 3, 8, 9, 14, 7, 5, 24, 1, 13, 16, 12, 5]
    s_key = key.copy()
    s_key.sort()
    print(f"key = {key}\ns_key = {s_key}")

    d = Dict()

    for i in range(N):
        d.insert(key[i])

    start_time = time.time()
    for i in range(N):
        result = d.search(s_key[i])
        print(f"목표 탐색 값: {s_key[i]} | 찾은 값: {result}")
        if result == -1 or result != s_key[i]:
            print('탐색 오류')
    end_time = time.time() - start_time
    print('\n선형 탐사법의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
    print('탐색 완료')
