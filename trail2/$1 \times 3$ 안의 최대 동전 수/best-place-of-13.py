n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

max_coin = 0

for i in range(n):
    for j in range(n-2):
        coin = 0

        for x in range(1):
            for y in range(3):
                coin += grid[i+x][j+y]

                if max_coin < coin:
                    max_coin = coin

print(max_coin)