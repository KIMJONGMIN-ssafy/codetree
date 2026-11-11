n = int(input())
grid = [list(input()) for _ in range(n)]

# Please write your code here.
coin =[]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            start = (i,j)
            
        elif grid[i][j] == 'E':
            end = (i,j)

        elif grid[i][j].isdigit():
            coin.append((int(grid[i][j]),i,j))
coin.sort()

def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

ans = float('inf')
def dfs(here, cnt, now, total):
    global ans
    if cnt == 3:
        total += dist(now, end)
        ans = min(ans,total)
        return

    for k in range(here, len(coin)):
        co, x, y = coin[k]

        next = (x,y)
        dis = dist(now, next)

        dfs(k+1, cnt+1, next, total+dis)

dfs(0,0,start,0)

if ans != float('inf'): 
    print(ans)
if ans == float('inf'):
    print(-1)
        


