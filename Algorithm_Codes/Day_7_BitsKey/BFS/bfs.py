import queue

# --------------------------------------------------------------------
#
# [실행 예]
# --------------------------------------------------------------------
# dfs(0) : 0 1 3 4 2 5
# dfs(1) : 1 0 2 4 3 5
# dfs(2) : 2 0 1 3 4 5
# dfs(3) : 3 0 1 2 4 5
# dfs(4) : 4 0 1 3 5 2
# dfs(5) : 5 3 0 1 2 4
# --------------------------------------------------------------------


# 구현
def bfs(v):
    pass

if __name__ == "__main__":
    q = queue.Queue()
    n = 6
    a = [[1, 2, 3, 4, None], [0, 3, None], [0, 4, None], [0, 1, 4, 5, None], [0, 2, 3, 5, None], [3, 4, None]]
    for i in range(n):
        visited = [False] * n
        print('bfs(%d) : ' % i, end='')
        bfs(i)
        print()
