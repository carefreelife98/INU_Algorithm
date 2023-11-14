def dfs(start, visited=None):
    if visited is None:
        visited = set()
    if start not in visited:
        print(start, end=" ")
        visited.add(start)
        for neighbor in a[start]:
            if neighbor is None:
                continue
            if neighbor not in visited:
                dfs(neighbor, visited)

if __name__ == "__main__":
    n = 6
    a = [[1, 2, 3, 4, None], [0, 3, None], [0, 4, None], [0, 1, 4, 5, None], [0, 2, 3, 5, None], [3, 4, None]]
    for i in range(n):
        # visited = [False] * n
        print('dfs(%d) : ' % i, end='')
        dfs(i)
        print()
