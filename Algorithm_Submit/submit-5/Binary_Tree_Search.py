import random, time
import sys


class node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class Dict:
    def __init__(self):
        self.x = self.p = node
        self.z = node(key=0, left=0, right=0)
        self.z.left = self.z
        self.z.right = self.z
        self.head = node(key=0, left=0, right=self.z)

    def search(self, search_key):
        # x = Root Node
        x = self.head.right
        parents = x

        # 탐색 알고리즘
        while x != self.z:
            # rs(현재 노드 x, 부모 노드 parents) - 현재 노드와 그 부모 노드를 튜플로서 반환. (Check 위해서)
            rs = (x, parents)

            if x.key == search_key:
                # print(f"x.key({x.key}) == search_key({search_key})")
                return rs
            elif x.key < search_key:
                parents = x
                x = x.right
            else:
                parents = x
                x = x.left
        return -1

    def insert(self, v):
        x = p = self.head
        while x != self.z:
            p = x
            if x.key == v:
                return
            if x.key > v:
                x = x.left
            else:
                x = x.right
        x = node(key=v, left=self.z, right=self.z)
        if p.key > v:
            p.left = x
        else:
            p.right = x

    def check(self, search_key):
        rs = self.search(search_key)
        if rs[0] == rs[1]:
            print(f"root node : root key = {rs[0].key}, parents key = {rs[1].key}")
            return True
        if rs[0] == rs[1].left:
            return rs[0].key <= rs[1].key
        elif rs[0] == rs[1].right:
            return rs[0].key >= rs[1].key
        else:
            print("이진 트리 Error 발생")
            return False


if __name__ == "__main__":
    for n in range(1, 4):
        N = 5000 * n
        key = list(range(1, N + 1))
        s_key = list(range(1, N + 1))
        print(f"\n-----------------------N = {N}-----------------------")
        for y in range(1, 4):
            d = Dict()
            if y == 1:
                random.shuffle(key)
                print(f"랜덤 배열 : {key[:5]} ...")
            elif y == 2:
                key.sort()
                print(f"정렬되어 있는 배열 : {key[:5]} ...")
            else:
                key.sort(reverse=True)
                print(f"역순으로 정렬된 배열 : {key[:5]} ...")

            # 이진 탐색 트리 삽입
            for i in range(N):
                d.insert(key[i])

            # 이진 탐색 트리 정확성 검사
            for i in range(N):
                if not d.check(key[i]):
                    print(f"이진 트리가 잘못 생성되어 종료합니다. key = {key[i]}")
                    sys.exit(1)

            print("이진 트리가 정상적으로 생성 되었습니다.")

            # print("이진 트리가 정상적으로 생성 되었습니다.")

            # 이진 탐색 트리 실행
            start_time = time.time()
            for i in range(N):
                result = d.search(s_key[i])[0].key
                if result == -1 or result != s_key[i]:
                    print('탐색 오류\n')
            end_time = time.time() - start_time

            # 이진 탐색 트리 결과
            print('이진 트리 탐색의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
            print('탐색 완료\n')
