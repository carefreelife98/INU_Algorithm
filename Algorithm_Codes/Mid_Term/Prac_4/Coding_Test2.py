N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * N
S[0] = A[0]
for i in range(1, N):
    S[i] = S[i-1] + A[i]

print()
# print('S = %s'%S)
count = 0
C = [0] * M

for i in range(N):
    R = S[i] % M
    if R == 0:
        count += 1
    C[R] += 1

# print('C = %s'%C)
for i in C:
    if i > 0:
        count += i * (i - 1) // 2

print(count)
