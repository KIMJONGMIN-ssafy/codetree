a, b = map(int, input().split())

# Please write your code here.

def sosu(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


def jjaksu(n):
    ans = 0

    for j in str(n):
        ans += int(j)

    return ans %2 == 0

cnt = 0

for k in range(a, b+1):
    if sosu(k) and jjaksu(k):
        cnt += 1

print(cnt)