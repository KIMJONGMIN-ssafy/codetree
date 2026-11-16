r, c = map(int, input().split())
grid = [input().split() for _ in range(r)]

cnt = 0

for i in range(1, r-1):
    for j in range(1, c-1):
        for k in range(i+1, r-1):
            for q in range(j+1, c-1):

                if grid[0][0] != grid[i][j]:
                    if grid[i][j] != grid[k][q]:
                        if grid[k][q] != grid[r-1][c-1]:
                            cnt += 1

print(cnt)