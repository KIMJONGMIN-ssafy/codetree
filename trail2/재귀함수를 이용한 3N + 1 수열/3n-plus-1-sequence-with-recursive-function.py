n = int(input())

# Please write your code here.

def go(a):
    global cnt
    if a == 1:
        return cnt
    
    if a%2 ==0:
        a = a//2
        cnt += 1
    elif a%2 ==1:
        a= a*3+1
        cnt += 1

    go(a)

cnt = 0
go(n)
print(cnt)