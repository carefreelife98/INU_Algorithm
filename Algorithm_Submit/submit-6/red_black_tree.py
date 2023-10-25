import random
import time

black = 0
red = 1

# 루트나 외부 노드는 모두 블랙
# 루트에서 외부 노드까지의 경로 상에는 2개의 연속된 레드 노드가 포함되지 않음
# 루트에서 각 외부 노드까지의 경로에 있는 블랙 노드의 수는 모두 같음
# 동일한 키를 가지는 레코드는 노드의 왼쪽과 오른쪽에 모두 올 수 있음
# 동일한 키가 여러 개 있을 때 주어진 키를 갖는 모든 노드를 찾는 것이 어려움

class node:
    def __init__(self, color, key=None, left=None, right=None):
        self.color = color
        self.key = key
        self.left = left
        self.right = right

class Dict:
    z = node(color=black, key=0, left=0, right=0)
    z.left = z
    z.right = z
    head = node(color=black, key=0, left=0, right=z)

    def search(self, search_key):
        x = self.head.right
        while x != self.z:
            if x.key == search_key:
                return x.key
            if x.key > search_key:
                x = x.left
            else:
                x = x.right
        return -1

    def insert(self, v):
        x = p = g = self.head
        while x != self.z:
            gg = g
            g = p
            p = x
            if x.key == v:
                return
            if x.key > v:
                x = x.left
            else:
                x = x.right
            if x.left.color and x.right.color:
                # x: Root | p: Root 복제본 | g: Head | gg: head | v: key
                self.split(x, p, g, gg, v)

        x = node(color=red, key=v, left=self.z, right=self.z)

        if p.key > v:
            p.left = x
        else:
            p.right = x
        self.split(x, p, g, gg, v)
        self.head.right.color = black

    def split(self, x, p, g, gg, v):
        x.color = red
        x.left.color = black
        x.right.color = black
        if p.color:
            g.color = red
            if (g.key > v) != (p.key > v):
                p = self.rotate(v, g)
            x = self.rotate(v, gg)
            x.color = black

    # 회전 알고리즘
    def rotate(self, v, y):
        if y.key > v:
            c = y.left
        else:
            c = y.right
        if c.key > v:
            gc = c.left
            c.left = gc.right
            gc.right = c
        else:
            gc = c.right
            c.right = gc.left
            gc.left = c
        if y.key > v:
            y.left = gc
        else:
            y.right = gc
        return gc

        # gc = c.right
        # c.right = gc.left
        # gc.left = c
        # y.left = gc

    def check(self, search_key):
        print(f"키 : {search_key}")
        x = p = self.head.right
        while (x != self.z):
            if x.color == 0:
                str_color = 'black'
            else:
                str_color = 'red'
            print(f"key : {x.key}, parents: {p.key}, color : {str_color}")
            p = x
            if x.key > search_key:
                x = x.left
            else:
                x = x.right

if __name__ == "__main__":
    for n in range(1, 4):
        N = n * 5000
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
            for i in range(0, N):
                d.insert(key[i])
                # d.check(key[i])
            start_time = time.time()
            for i in range(N):
                result = d.search(s_key[i])
                if result == -1 or result != s_key[i]:
                    print(f"탐색 오류: result = {result}, s_key[{i}] = {s_key[i]}")
            end_time = time.time() - start_time
            print('레드 블랙 트리 탐색의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
            print('탐색 완료\n')
