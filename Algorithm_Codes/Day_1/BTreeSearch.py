import random
def binary_search(l, key, left, right):
    if left <= right:
        mid = int((left+right) / 2)
        if key == l[mid]:
            return mid
        elif key < l[mid]:
            return binary_search(l, key, left, mid - 1)
        else:
            return binary_search(l, key, mid+1, right)
    else:
        return -1

if __name__ == "__main__":
    n = int(input("자연수의 개수 입력: "))
    a = []
    for i in range(n+1):
        temp = random.randint(1, 100)
        a.append(temp)
    a.sort()

    print(f"리스트 생성 : {a}")
    k = int(input("key 를 입력하세요: "))
    print(f'입력된 key {k}의 index는 {binary_search(a, k, 0, n - 1)} 입니다.')
