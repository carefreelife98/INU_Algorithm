class PQ:
    def __init__(self):
        self.heap = [0]*100
        self.info = [0]*100
        self.n = 0

    def insert(self, v, x):
        self.n += 1
        i = self.n
        while True:
            if i == 1: break
            if v >= self.heap[int(i/2)]: break
            self.heap[i] = self.heap[int(i/2)]
            self.info[i] = self.info[int(i/2)]
            i = int(i/2)
        self.heap[i] = v
        self.info[i] = x

    def remove(self):
        x = self.info[1]
        temp_v = self.heap[self.n]
        temp_x = self.info[self.n]
        self.n -= 1
        i = 1
        j = 2
        while j <= self.n:
            if (j < self.n) and (self.heap[j] > self.heap[j+1]):
                j += 1
            if temp_v <= self.heap[j]: break
            self.heap[i] = self.heap[j]
            self.info[i] = self.info[j]
            i = j
            j *= 2
        self.heap[i] = temp_v
        self.info[i] = temp_x
        return x

    def isEmpty(self):
        if self.n == 0: return True
        else: return False

def index(c):
    if ord(c) == 32:
        return 0
    else:
        return (ord(c)-64)

def makeHuffman(t, m):
    for i in range(m):
        count[index(t[i])] += 1
    for i in range(27):
        if count[i]:
            pq.insert(count[i], i)
    i = 27
    while not pq.isEmpty():
        t1 = pq.remove()
        t2 = pq.remove()
        dad[i] = 0
        dad[t1] = i
        dad[t2] = -i
        count[i] = count[t1] + count[t2]
        if not pq.isEmpty():
            pq.insert(count[i], i)
        i += 1
    for k in range(27):
        i = x = 0
        j = 1
        if count[k]:
            q = dad[k]
            while q:
                if q < 0:
                    x += j
                    q = -q
                q = dad[q]
                j += j
                i += 1
        code[k] = x
        length[k] = i

def encode(t, m):
    huffman_code = ''
    for j in range(m):
        i = length[index(t[j])]
        while i > 0:
            huffman_code += str((code[index(t[j])] >> i - 1) & 1)
            i -= 1
    return huffman_code

def char(k):
    if k == 0: return chr(32)
    else: return chr(k+64)

def findDad(max_i, k):
    for i in range(max_i):
        if dad[i - 1] == k:
            # print(f"dad[i]({dad[i - 1]}) == k({k})")
            return i
    return -1

# 인코딩된 문자열들을 앞에서부터 읽어들여 root 노드로부터
# 0이 나오면 왼쪽 자식으로 이동
# 1이 나오면 오른쪽 자식으로 이동
# 단말 노드가 나올때까지 이를 반복.
# 단말 노드가 나온 경우 그 노드에 알맞은 알파벳을 출력한 후 다시 루트 노드로 돌아가서 반복
    # k 는 41부터 시작.
    # 허프만 코드가 0 이면 k 와 같은 절대값을 가진 양수 dad[k] 로 이동.
    # 1이면 음수 dad[k] 로 이동.
def decode(h):
    decoded_text = ""

    # k 배열 마지막 값 복사.
    k_idx = len(k) - 1
    temp = k[k_idx]
    temp_str = ""
    cp_h = h
    while len(cp_h) != 0:
        # k 와 같은 dad[k] 값이 없을 때 까지 이동.
        # 41
        # 이전 while loop 에서 변경된 k 배열 마지막 값 초기화
        k[k_idx] = temp
        toggle = False
        while k[k_idx] in dad:
            # 띄어쓰기 검출
            if k[k_idx] == 0:
                toggle = not toggle
                break

            # Huffman 코드가 0인 경우 양수
            if cp_h[0] == '0':
                k[k_idx] = dad.index(k[k_idx])

            # Huffman 코드가 1인 경우 음수
            else:
                k[k_idx] = dad.index(-(k[k_idx]))
            # Huffman code 첫 문자 삭제
            cp_h = cp_h[1:]

        if toggle:
            decoded_text += ' '
        else:
            decoded_text += chr(k[k_idx] + 64)
    return decoded_text


if __name__ == "__main__":
    text = 'VISION QUESTION ONION CAPTION GRADUATION EDUCATION'
    # text = 'A SIMPLE STRING TO BE ENCODED USING A MINIMAL NUMBER OF BITS'
    print(f"\nOriginal Text: {text}\n")

    count = [0]*100
    dad = [0]*100
    length = [0]*27
    code = [0]*27
    M = len(text)
    pq = PQ()
    makeHuffman(text, M)

    # print(f"count[k]: {count} \ndad[k]: {dad}\n")

    # print(f"code[k]: {code} \nlength[k]: {length}\n")

    k = []
    print(f"count={len(count)}, {count}")
    for i in range(len(count)):
        if count[i] != 0:
            k.append(i)
    print(len(k), k)
    h = encode(text, M)
    print(f"Encoded Text: {len(h)},{h}\n")
    d = decode(h)
    print(f"Decoded Text: {d}\n")
