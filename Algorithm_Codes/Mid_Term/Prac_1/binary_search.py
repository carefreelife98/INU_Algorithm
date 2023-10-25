import random

def binarySearch(a, key, left, right):
    if left <= right:
        mid = (left + right) // 2
        if key == a[mid]:
            return mid
        elif key < a[mid]:
            return binarySearch(a, key, left, mid-1)
        else:
            return binarySearch(a, key, mid+1, right)
    else:
        return -1

A = []
for i in range(10):
    A.append(random.randint(1, 50))
A.sort()
print(A)

key = int(input('탐색 키 입력 : '))
res = binarySearch(A, key, 0, len(A) - 1)
if res == -1:
    print('탐색 키를 갖는 원소를 찾을 수 없음')
else:
    print(res+1, '번째 원소')
