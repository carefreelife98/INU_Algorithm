def bruteForce(p, t, k):
    M = len(p); N = len(t)
    i, j = k, 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == M:
        return i - M
    else:
        return i

def find_email(pat, txt, k):
    M = len(pat); N = len(txt)

    while True:
        pos = bruteForce(pat, txt, k)
        k = pos + M
        if k < N:
            print('패턴이 나타난 위치 : ', pos)
            char = ''
            str_to_find = ""
            while char != "\"":
                char = txt[pos]
                str_to_find += txt[pos]
                pos += 1
            str_to_find = str_to_find.removesuffix("\"")
            print(str_to_find)
        else:
            break
    print('스트링 탐색 종료')

if __name__ == "__main__":
    fin = open('email.html', encoding='UTF-8')
    text = fin.read()
    find_email("mailto:", text, 0)
