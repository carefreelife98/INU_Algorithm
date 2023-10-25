import random
import time


class Dict:
    def __init__(self):
        self.a = [-1] * M

    def insert(self, v):
        x = self.hash(v)
        u = self.hash2(v)
        print(f"\ninsert {v} | Hash 값: {x} | Hash(2) 값: {u}")

        if self.a[x] == -1:
            self.a[x] = v
            print(f"Hashing, 바로 할당. index:{x} | value:{self.a[x]} ")
        else:
            if x + u < len(self.a):
                d = x + u
            else:
                d = x + u - len(self.a)

            while self.a[d] != -1:
                print(f"충돌(index{d} 에 {self.a[d]}값 존재). d값 Re-DoubleHashing")
                d += u
                if d >= len(self.a):
                    d -= len(self.a)
            self.a[d] = v
            print(f"빈 공간 찾음, 현재 위치 {d}에 {self.a[d]}값 할당.")

    def search(self, v):
        x = self.hash(v)
        u = self.hash2(v)
        temp = self.a.copy()

        if self.a[x] == v:
            print(f"{v}에 대한 Hash 값 바로 찾음, index[{x}]: {self.a[x]}, 반환")
            return self.a[x]
        else:
            print(f"\n----------------------------Double Hashing 진행----------------------------")
            print(f"충돌(index[{x}] 에 {self.a[x]}값 존재). d값 Re-DoubleHashing")
            if x + u < len(self.a):
                dh = x + u
            else:
                dh = x + u - len(self.a)
            max_loop = 0
            while self.a[dh] != v:
                print(f"충돌(index[{dh}] 에 {self.a[dh]}값 존재). d값 Re-DoubleHashing")
                dh += u
                if dh >= len(self.a):
                    dh -= len(self.a)
                max_loop += 1
                if len(self.a) < max_loop:
                    print(f"값: {v} 를 찾지 못했습니다.")
                    break
            print(f"{v} 에 대한 Hash 값 탐색 완료 (Double Hashing), index[{dh}]: {self.a[dh]}, 반환")
            print(f"----------------------------Double Hashing 끝----------------------------\n")
            return self.a[dh]

    def hash(self, v):
        return v % M

    def hash2(self, v):
        return 8 - (v % 8)


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
    print("----------------------------key list----------------------------")
    print(f"key = {key}\ns_key = {s_key}")
    print("----------------------------key list----------------------------\n")

    d = Dict()
    print("=============================[Start insert]=============================")
    for i in range(N):
        d.insert(key[i])
    print("--------------------------------------------------------------------")
    print(f"d after insert = {d.a}")
    print("=============================[End insert]=============================\n")
    print("=============================[Start search]=============================")
    start_time = time.time()
    for i in range(N):
        result = d.search(s_key[i])
        if result == -1 or result != s_key[i]:
            print('탐색 오류')
    end_time = time.time() - start_time
    print("=============================[End search]=============================\n")
    print('이중 해싱의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
    print('탐색 완료')
