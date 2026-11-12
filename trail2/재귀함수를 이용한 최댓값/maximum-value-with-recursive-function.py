n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

ans = 0

def go(arr):
    global ans
    if arr == n:
        return

    for i in range(n):
        if arr[i] > ans:
            ans = arr[i]
        

go(arr)
print(ans)