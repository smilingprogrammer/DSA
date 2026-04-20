import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    visited = [[False] * m for _ in range(n)]
    best = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0 and not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                volume = 0

                while stack:
                    x, y = stack.pop()
                    volume += grid[x][y]

                    if x > 0 and grid[x - 1][y] > 0 and not visited[x - 1][y]:
                        visited[x - 1][y] = True
                        stack.append((x - 1, y))

                    if x + 1 < n and grid[x + 1][y] > 0 and not visited[x + 1][y]:
                        visited[x + 1][y] = True
                        stack.append((x + 1, y))

                    if y > 0 and grid[x][y - 1] > 0 and not visited[x][y - 1]:
                        visited[x][y - 1] = True
                        stack.append((x, y - 1))

                    if y + 1 < m and grid[x][y + 1] > 0 and not visited[x][y + 1]:
                        visited[x][y + 1] = True
                        stack.append((x, y + 1))

                best = max(best, volume)
    # print('\n')
    # print('=====')
    print(best)
    # print('\n')
    # print('=====')