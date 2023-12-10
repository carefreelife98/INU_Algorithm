import sys
dna = ['A', 'C', 'G', 'T']
def search(s, p, c):
    usable_case = 0
    for i in range(len(s)):
        elem_count = [0, 0, 0, 0]
        for window in s[i:i+p]:
            if window == 'A':
                elem_count[0] += 1
            elif window == 'C':
                elem_count[1] += 1
            elif window == 'G':
                elem_count[2] += 1
            elif window == 'T':
                elem_count[3] += 1
        if elem_count == c:
            usable_case += 1
    return usable_case

if __name__ == "__main__":
    S, P = sys.stdin.readline().split(' ')
    P = int(P)
    text = sys.stdin.readline()
    count = sys.stdin.readline().split(' ', 4)
    count = list(map(int, count))
    result = search(text, P, count)
    print(result)
