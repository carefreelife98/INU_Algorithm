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
        self.key = key
        self.b = None
        self.left = None
        self.right = None

class Dict:
    itemMin = bitskey(0)
    head = node(itemMin)
    head.b = maxb
    head.left = head.right = head

    def search(self, v):
        v = bitskey(v)
        p = self.head
        x = self.head.left
        while p.b > x.b:
            p = x
            if self.bits(v, x.b, 1):
                x = x.right
            else:
                x = x.left
        if v.get() != x.key.get():
            return self.itemMin
        return x.key

    def insert(self, v):
        v = bitskey(v)
        i = maxb
        p = self.head
        t = self.head.left
        while p.b > t.b:
            p = t
            if self.bits(v, t.b, 1):
                t = t.right
            else:
                t = t.left
        if v.get() == t.key.get():
            return
        while self.bits(t.key, i, 1) == self.bits(v, i, 1):
            i -= 1
        p = self.head
        x = self.head.left
        while p.b > x.b > i:
            p = x
            if self.bits(v, x.b, 1):
                x = x.right
            else:
                x = x.left
        t = node(self.itemMin)
        t.key = v
        t.b = i
        if self.bits(v, t.b, 1):
            t.left = x
            t.right = t
        else:
            t.left = t
            t.right = x

        if self.bits(v, p.b, 1):
            p.right = t
        else:
            p.left = t

    def bits(self, item, bit, cmp):
        if item.bits(bit, 1) == cmp:
            return 1
        else:
            return 0

    # 구현
    def check(self, v):
        v = bitskey(v)
        p = self.head
        x = self.head.left
        parents = 0
        while p.b > x.b:
            p = x
            if self.bits(v, x.b, 1):
                if parents != x.key.get():
                    parents = x.key.get()
                x = x.right
                # print(f"parents:{parents} number:{x.b} and key = {x.key.get()}")
            else:
                if parents != x.key.get():
                    parents = x.key.get()
                x = x.left
                # print(f"parents:{parents} number:{x.b} and key = {x.key.get()}")
        if v.get() != x.key.get():
            print(f"return {self.itemMin}")
        print(f"key: {x.key.get()}, parents: {parents} , number: {x.b}")

if __name__ == "__main__":
    N = 7
    key = [1, 19, 5, 18, 3, 26, 9]
    s_key = [1, 19, 5, 18, 3, 26, 9]
    # key = [7, 20, 17, 4, 9, 21, 23, 13]
    # s_key = [7, 20, 17, 4, 9, 21, 23, 13]
    s_key.sort()

    d = Dict()
    for i in range(N):
        d.insert(key[i])
    print(key)
    # for i in range(N):
    #     print(f"search: [{s_key[i]}], find: [{d.search(s_key[i]).get()}]")
    for i in range(N):
        d.check(s_key[i])