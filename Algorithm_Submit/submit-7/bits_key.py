class bitskey:
    def __init__(self, x):
        self.x = x

    def get(self):
        return self.x

    def bits(self, k, j):
        # 알고리즘:
        #   1. k 만큼 우측 shift 이동 -> k 번째 Bit 가 마지막 비트가 된다.
        #   2. 11111 을 j 만큼 좌측 shift -> j 만큼 0이 생성.
        #      j = 1 이므로 가장 마지막 비트가 0이 됨.
        #   3. 11110 을 NOT 연산을 통해 00001 으로 변환.
        #   4. 00001 과 0000k 를 AND 연산.
        #      k 가 1 이면 1, 0 이면 0을 반환.
        #   5. 따라서 bits(k, 1) 을 수행 할 시 k번째 비트 값을 알 수 있음.
        return (self.x >> k) & ~(~0 << j)

if __name__ == "__main__":
    a = int(input('입력 : '))
    while a != 999:
        # bitskey data type 으로 변환.
        v = bitskey(a)
        print('키값 :',  v.get())

        # 4번 비트
        print(v.bits(4, 1))

        # 3번 비트
        print(v.bits(3, 1))
        print(v.bits(2, 1))
        print(v.bits(1, 1))
        print(v.bits(0, 1))
        a = int(input('a = '))
