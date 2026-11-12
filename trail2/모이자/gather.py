n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
ans = float('inf')

for i in range(n):
    total = 0
    for j in range(n):
        distance = abs(i-j)
        p_distance = distance*A[j]
        total += p_distance
    
    ans = min(ans, total)
print(ans)