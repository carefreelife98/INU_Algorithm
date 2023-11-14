# --------------------------------------------------------------------
# a = [[1, 2, 3, 4, None],
#      [0, 3, None],
#      [0, 4, None],
#      [0, 1, 4, 5, None],
#      [0, 2, 3, 5, None],
#      [3, 4, None]]
# --------------------------------------------------------------------

def dfs(visit, v):
    i = 0
    visit[v] = True
    print(v, end=" ")
    next_num = a[v][i]
    # print(f"next_num = {next_num}")
    node = a[next_num]
    print(next_num, end=" ")
    visit[next_num] = True
    while visit.count(True) != len(visit):
        j = 0
        while node[j] is not None:
            if visit[node[j]] is False:
                print(node[j], end=" ")
                visit[node[j]] = True
            j += 1
        temp = node[j - 1]
        # print(temp)
        node = a[temp]



    # while visit.count(True) != len(visit):
    #     if l[v][i] is None:
    #         temp = l[v][i-1]
    #         node = l[]
    #         continue
    #     node = l[v][i]
    #     if not visit[node]:
    #         print(node, end=" ")
    #         visit[node] = True
    #     i += 1


if __name__ == "__main__":
    n = 6
    a = [[1, 2, 3, 4, None], [0, 3, None], [0, 4, None], [0, 1, 4, 5, None], [0, 2, 3, 5, None], [3, 4, None]]
    for i in range(n):
    # i = 0
        visited = [False] * n
        print('dfs(%d) : ' % i, end='')
        dfs(visited, i)
        print()
