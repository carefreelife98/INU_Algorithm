N, L = map(int, input().split())
A = list(map(int, input().split()))

D = []  # Di 값을 저장할 리스트

for i in range(N):
    # i가 L보다 크거나 같을 때부터 Di를 계산하고 저장
    if i >= L - 1:
        min_value = min(A[i - L + 1:i + 1])
        D.append(min_value)

# Di 출력
print(' '.join(map(str, D)))
