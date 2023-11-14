maxb = 5

class bitskey:
    def __init__(self, x):
        self.x = x

    def get(self):
        return self.x

    def bits(self, k, j):
        return (self.x >> k) & ~(~0 << j)

class node:
    def __init__(self, key):
        # 노드 생성 시 해당 노드 값이 0이면 bitskey = 0(0000) 으로 생성 및 말단 노드가 아닌 것으로 지정.
        if key.get() == 0:
            self.key = bitskey(0)
            self.external = False
        else :
            # 노드 생성 시 값이 존재하면 해당 노드의 값으로 설정하고 말단 노드로 지정.
            self.key = key
            self.external = True
        # 노드 생성 시 항상 자식 노드는 0
        self.left = 0
        self.right = 0

class Dict:
    itemMin = bitskey(0)
    head = 0
    head_check = False

    def search(self, v):
        v = bitskey(v)
        return self.searchR(self.head, v, maxb-1)

    def insert(self, v):
        v = bitskey(v)
        self.insertR(self.head, v, maxb-1)

    def insertR(self, h, v, d):
        # 헤드 노드가 없으면 생성
        if h == 0:
            h = node(v)
            if not self.head_check:
                self.head = h
            return h
        # 헤드 노드가 고유 값을 가진(0이 아닌) 말단 노드이면 ? v: 새로운 노드의 값
        if h.external:
            # 말단 노드로서 v 노드 생성 = leaf
            leaf = node(v)
            h = self.split(leaf, h, d)
            if not self.head_check:
                self.head = h
                self.head_check = True
            return h
        if v.bits(d, 1) == 0:
            h.left = self.insertR(h.left, v, d-1)
        else:
            h.right = self.insertR(h.right, v, d-1)
        return h

    def split(self, p, q, d):
        t = node(self.itemMin)
        # 00
        if ((p.key.bits(d, 1))*2 + (q.key.bits(d, 1))) == 0:
            t.left = self.split(p, q, d-1)
        # 01
        elif ((p.key.bits(d, 1))*2 + (q.key.bits(d, 1))) == 1:
            t.left = p
            t.right = q
        # 10
        elif ((p.key.bits(d, 1))*2 + (q.key.bits(d, 1))) == 2:
            t.right = p
            t.left = q
        # 11
        elif ((p.key.bits(d, 1))*2 + (q.key.bits(d, 1))) == 3:
            t.right = self.split(p, q, d-1)
        return t

    def searchR(self, h, v, d):
        if h == 0:
            return self.itemMin
        if v.get() == h.key.get():
            return v
        if v.bits(d, 1) == 0:
            print("left", end=" ")
            return self.searchR(h.left, v, d-1)
        else:
            print("right", end=" ")
            return self.searchR(h.right, v, d-1)

    # 구현
    def check(self, v):
        print(v, end=" ")
        v = bitskey(v)
        h = self.head
        d = maxb - 1
        if h == 0:
            return self.itemMin
        if v.get() == h.key.get():
            return v
        if v.bits(d, 1) == 0:
            print("left", end=" ")
            return self.searchR(h.left, v, d-1)
        else:
            print("right", end=" ")
            return self.searchR(h.right, v, d-1)


if __name__ == "__main__":
    N = 7
    key = [1, 19, 5, 18, 3, 26, 9]
    s_key = [1, 19, 5, 18, 3, 26, 9]
    s_key.sort()

    d = Dict()
    for i in range(N):
        d.insert(key[i])
    print(key)
    d.head.external = True
    for i in range(N):
        d.check(s_key[i])
        print("")
