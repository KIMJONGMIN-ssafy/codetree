n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
ans = 0

def dfs(start, cnt, result):
    global ans

    if cnt == m:
        ans = max(ans, result)
        return

    for i in range(start, n):
        dfs(i + 1, cnt + 1, result ^ A[i])

dfs(0, 0, 0)

print(ans)