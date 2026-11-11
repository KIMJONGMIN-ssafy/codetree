N, M = map(int, input().split())

# Please write your code here.

def dfs(n):
    
    if len(ans) == M:
        print(*ans)
        return

    for i in range(n, N+1):
        ans.append(i)
        dfs(i+1)
        ans.pop()

ans = []
dfs(1)


