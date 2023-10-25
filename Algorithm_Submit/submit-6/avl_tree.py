import random, time

class node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Dict:
    def __init__(self):
        self.node = None
        self.height = 0
        self.balance = 0

    def search(self, search_key):
        x = self.node
        while x is not None:
            if x.key == search_key:
                return x.key
            if x.key > search_key:
                x = x.left.node
            else:
                x = x.right.node
        return -1

    def insert(self, v):
        x = self.node
        if x is None:
            self.node = node(v)
            self.node.left = Dict()
            self.node.right = Dict()

        elif x.key > v:
            self.node.left.insert(v)

        else:
            self.node.right.insert(v)

        self.check_balance()

    def check_balance(self):
        self.update_heights(False)
        self.update_balances(False)

        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.rotate_left()
                self.rotate_right()

            else:
                if self.node.right.balance > 0:
                    self.node.right.rotate_right()
                self.rotate_left()

            self.update_heights()
            self.update_balances()

    def rotate_right(self):
        g = self.node
        p = g.left.node
        x = p.right.node
        self.node = p
        p.right.node = g
        g.left.node = x

    def rotate_left(self):
        g = self.node
        p = g.right.node
        x = p.left.node
        self.node = p
        p.left.node = g
        g.right.node = x

    def update_heights(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_heights()
                if self.node.right is not None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height, self.node.right.height) + 1
        else:
            self.height = 0

    def update_balances(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_balances()
                if self.node.right is not None:
                    self.node.right.update_balances()
            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def check(self, search_key):
        x = self.node
        temp = None  # 부모 노드를 저장할 변수
        while x is not None:
            if x.key == search_key:
                if temp is not None:
                    print(f"탐색 성공 (key={x.key}|search_key={search_key}) | Parents = {temp.key}")
                else:
                    print(f"key = {x.key} == search_key = {search_key}, No Parent (Root)")
                break  # 원하는 노드를 찾았으므로 루프 종료
            temp = x  # 현재 노드를 부모 노드로 저장
            if search_key < x.key:
                x = x.left.node
            else:
                x = x.right.node
        if x is None:
            print(f"{search_key}는 이진 트리에 존재하지 않습니다.")

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
            print('AVL 트리 탐색의 실행 시간 (N = %d) : %0.3f'%(N, end_time))
            print('탐색 완료\n')

# d = Dict()
    # key = int(input('키 : '))
    # while key != 999:
    #     d.insert(key)
    #     d.check(key)
    #     key = int(input('키 : '))