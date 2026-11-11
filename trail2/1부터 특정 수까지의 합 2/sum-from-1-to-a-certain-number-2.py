N = int(input())

# Please write your code here.
ans = 0

def go(a):
    global ans
    if a > N:
        return
    
    ans += a
    go(a+1)

go(1)

print(ans)