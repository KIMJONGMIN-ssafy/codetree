a, b = map(int, input().split())

# Please write your code here.

def ans(a,b):
    global cnt
    for i in range(min(a,b), max(a,b)+1):
        if '3' in str(i) or '6' in str(i) or '9' in str(i):
            cnt +=1
        elif i%3 ==0:
            cnt +=1

cnt = 0

ans(a,b)

print(cnt)