import random, time

k = 0
class node:
    def __init__(self, key=None):
        self.key = key
        global k
        k += 1
        # print(f"key{k} = {key}")

class Dict:
    def __init__(self):
        self.a = []

    # 탐색 알고리즘
    def search(self, search_key, n):
        # for i in range(n):
        #     if self.a[i].key == search_key:
        #         return i
        #     else:
        #         return -1
        i = 0
        while i <= n and self.a[i].key != search_key:
            i += 1
        if i == n:
            return -1
        else:
            return i


    def insert(self, v):
        self.a.append(node(v))

if __name__ == "__main__":
    for x in range(1, 4):
        N = 5000 * x
        key = list(range(1, N + 1))
        s_key = list(range(1, N + 1))
        random.shuffle(key)

        d = Dict()
        for i in range(N):
            d.insert(key[i])

        print(f"size of d.a[] = {len(d.a)}")

        start_time = time.time()
        for i in range(N):
            result = d.search(s_key[i], N)
            # print(f"key[{result}] = {key[result]}, s_key[{i}] = {s_key[i]}")
            if result == -1 or key[result] != s_key[i]:
                print('탐색 오류')
        end_time = time.time() - start_time
        print('순차 탐색의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
        print('탐색 완료')
