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
    except Exception as e:
        print(f"Error Occurred: [{e}]")

def gen_coordinate(a, n, m):
    print(f"\n위에서 생성된 {n} X {n} 행렬에서 다음 {m}개의 좌표 구간 합 결과를 반환:")

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
        for j in range(y1, y2 + 1):
            total += l[i][j]
            print(f"total = {total}, l[{i}][{j}] = {l[i][j]}")
    return total

def sum_result(matrix, coordinate: []):
    try:
        for idx, value in enumerate(coordinate):
            print(f"\n {idx + 1} / {len(coordinate)} 번째 좌표 [{value}] 간 값의 합 계산 시작")
            x1, y1, x2, y2 = 0, 0, 0, 0
            for j in range(4):
                match j:
                    case 0: x1 = value[j]
                    case 1: y1 = value[j]
                    case 2: x2 = value[j]
                    case 3: y2 = value[j]
            print(f"(x1, y1) = ({x1}, {y1}), (x2, y2) = ({x2}, {y2})")
            if x1 == x2 and y1 == y2:
                print("두 좌표가 같습니다.")
                total = matrix[x1][y1]
            else:
                min_x, max_x = min(x1, x2), max(x1, x2)
                min_y, max_y = min(y1, y2), max(y1, y2)
                total = sum_mat_bydiff(matrix, min_x, min_y, max_x, max_y)
            print(f"Total = {total}")
    except Exception as e:
        print(f"Error Occurred: [{e}]")

if __name__ == "__main__":
    print("n, m  입력:")
    n, m = map(int, input().split())

    mat = gen_matrix(n, m)
    co_ordinate = gen_coordinate(mat, n, m)
    sum_result(mat, co_ordinate)
