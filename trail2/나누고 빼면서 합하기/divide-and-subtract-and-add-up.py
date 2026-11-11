n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

def gogo(a):
    global ans
    ans.append(a)
    while a >1:
        if a % 2 ==1:
            a = a-1
            ans.append(a)
        if a % 2 == 0:
            a = a//2
            ans.append(a)

    
ans = []
gogo(m)
ans2 = []

for i in ans:
    ans2.append(A[i-1])

print(sum(ans2))


    