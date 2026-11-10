a, b = map(int, input().split())

# Please write your code here.

def answer(a,b):
    global cnt
  
    for i in range(a, b+1):
        if i %2 ==0:
            continue
        if i%10 == 5:
            continue
        if i%3 ==0 and i%9 !=0:
            continue

        cnt +=1


cnt = 0
answer(a,b)

print(cnt)