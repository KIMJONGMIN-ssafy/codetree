n = int(input())
num = list(map(int, input().split()))

# Please write your code here.

visited = [False]*(2*n)

def hapcha(start, cnt):
    global ans
    if cnt == n:
        a= []
        b= []
        
        for i in range(2*n):
            if visited[i]:
                a.append(num[i])
            else:
                b.append(num[i])

        ans = min(ans, abs(sum(a) - sum(b)))
        return

    for j in range(start, 2*n):
        if not visited[j]:
            visited[j] = True
            hapcha(j+1, cnt+1)
            visited[j] = False

ans = float('inf')

hapcha(0,0)
print(ans)
