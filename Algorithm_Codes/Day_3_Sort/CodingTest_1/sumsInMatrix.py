import random
def gen_matrix(n, m):
    try:
        # (n,m) 범위 설정 확인
        if 1 >= n >= 1024 or 1 >= m >= 100000:
            return "1 <= n <= 1024, 1 <= m <= 100,000 범위가 잘못되었습니다."
        print()
        print(f"{n} X {n} 행렬 생성:")
        a = []
        for _ in range(n):
            b = []
            for i in range(n):
                num = random.randint(1, 9)
                b.append(num)
            a.append(b)
        for i in a:
            print(i)
        return a
    except():
        print("Error Occured!! \n")

def gen_coordinate(a, n, m):
    print(f"\n{n} X {n} 행렬에서 {m}개의 좌표 구간 합 결과를 반환:")

    xy = []
    for i in range(m):
        temp = []
        for j in range(4):
            temp.append(random.randint(0, n - 1))
        xy.append(temp)
    for a in xy:
        print(a)
    return xy

def sum_mat_bydiff(l, x1, y1, x2, y2):
    total = 0
    for i in range(x1, x2 + 1):
        print("loop1")
        for j in range(y1, y2 + 1):
            print("loop2")
            total += l[i][j]
            print(f"total = {total}, l[i][j] = {l[i][j]}")
    return total

def sum_result(matrix, coordinate: []):
    # try:
    for i in coordinate:
        print(f"\n\n{i}, coordinate = {coordinate}")
        x1, y1, x2, y2 = 0, 0, 0, 0
        for j in range(4):
            match j:
                case 0: x1 = i[j]
                case 1: y1 = i[j]
                case 2: x2 = i[j]
                case 3: y2 = i[j]
        print(f"x1 = {x1}, y1 = {y1}, x2 = {x2}, y2 = {y2}")
        if x1 == x2 and y1 == y2:
            print("두 좌표가 같습니다.")
            total = matrix[x1][y1]
        elif (x1, y1) > (x2, y2):
            print("x1, y1 이 더 큽니다.")
            total = sum_mat_bydiff(matrix, x2, y2, x1, y1)
        else:
            print("x2, y2 이 더 큽니다.")
            total = sum_mat_bydiff(matrix, x1, y1, x2, y2)
        print(f"Total = {total}")
    # except e:
    #     print(f"Error Occured!! : sum_result, {e}")

if __name__ == "__main__":
    print("n, m  입력:")
    n, m = map(int, input().split())

    mat = gen_matrix(n, m)
    co_ordinate = gen_coordinate(mat, n, m)
    sum_result(mat, co_ordinate)


# (absx, absy) 좌표가 가리키는 곳이 시작지점.
            # 해당 점부터 absx > absy 일 시 y축을 차이만큼 더 증가시켜 반복
            # absx < absy       "       x축          "
# x1, x2 = 0, 0
            # y1, y2 = 0, 0
            # for j in range(4):
            #     match j:
            #         case 0:
            #             x1 = cord[0]
            #         case 1:
            #             y1 = cord[1]
            #         case 3:
            #             x2 -= cord[2]
            #         case 4:
            #             y2 -= cord[3]