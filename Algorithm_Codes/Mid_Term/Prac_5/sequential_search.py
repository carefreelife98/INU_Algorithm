class node:
    def __init__(self, key=None):
        self.key = key

class Dict:
    def __init__(self):
        Dict.a = []

    def search(self, search_key, n):
        i = 0
        while i < n and Dict.a[i].key != search_key:
            i += 1
        if i == n:
            return -1
        else:
            return i

    def insert(self, v):
        Dict.a.append(node(v))

N = 8
key = [2, 1, 7, 8, 6, 3, 5, 4]
print('키 리스트: ', key)
print()
d = Dict()
for i in range(N):
    d.insert(key[i])
s_key = int(input('탐색 키 (종료시 999) : '))
while s_key != 999:
    res = d.search(s_key, N)
    if  res == -1:
        print('탐색 키 없음')
    else: print('%d 번째 원소'%(res+1))
    print()
    s_key = int(input('탐색 키 (종료시 999) : '))
