import heapq
from collections import deque

def using_heap(N, L, hq, answer):
    for i in range(N):
        heapq.heappush(hq, (A[i], i))
        while hq[0][1] < i - L + 1:
            heapq.heappop(hq)
        answer.append(hq[0][0])

    print(" ".join(map(str, answer)))

def using_deque(N, L, q, i):
    while i < N:
        while q and q[-1][1] > A[i]:
            q.pop()
        q.append((i, A[i]))
        i += 1
        if i - q[0][0] > L:
            q.popleft()
        print(q[0][1], end=' ')


if __name__ == "__main__":
    N, L = map(int, input().split())
    A = list(map(int, input().split()))

    # using Heap
    hq = []
    answer = []

    # using Deque
    q = deque()
    i = 0

    using_heap(N, L, hq, answer)
    using_deque(N, L, hq, i)
