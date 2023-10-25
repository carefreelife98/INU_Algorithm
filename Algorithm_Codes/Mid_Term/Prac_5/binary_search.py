class node:
    def __init__(self, key=None):
        self.key = key

class Dict:
    def __init__(self):
        Dict.a = []

    def search(self, search_key, n):
        left = 0
        right = n - 1
        while right >= left:
            mid = (left + right) // 2
            if Dict.a[mid].key == search_key:
                return mid
            if Dict.a[mid].key > search_key:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def insert(self, v):
        Dict.a.append(node(v))

N = 8
key = [1, 3, 5, 7, 9, 11, 13, 15]
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
