import random, time
class node:
    def __init__(self, key=None):
        self.key = key

class Dict:
    def __init__(self):
        self.a = []

    # 탐색 알고리즘
    def search(self, search_key, n):
        r = len(self.a) - 1
        l = 0
        while l <= r:
            mid = (l + r) // 2
            if search_key == self.a[mid].key:
                # print(f"search_key = {search_key}, self.a[mid].key = {self.a[mid].key}, mid = {mid}")
                return mid
            elif search_key < self.a[mid].key:
                r = mid - 1
            else:
                l = mid + 1
        return -1

    def insert(self, v):
        self.a.append(node(v))

if __name__ == "__main__":
    for x in range(1, 4):
        N = 5000 * x
        key = list(range(1, N + 1))
        s_key = list(range(1, N + 1))
        random.shuffle(s_key)

        d = Dict()
        for i in range(N):
            d.insert(key[i])

        start_time = time.time()
        for i in range(N):
            result = d.search(s_key[i], N)
            if result == -1 or key[result] != s_key[i]:
                print('탐색 오류')
        end_time = time.time() - start_time
        print('이진 탐색의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
        print('탐색 완료')
