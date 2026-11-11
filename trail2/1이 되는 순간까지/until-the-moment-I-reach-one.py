N = int(input())

# Please write your code here.
def recall(a, cnt):
    
    if a == 1:
        print(cnt)
        return
    
    if a%2 ==0:
        recall(a//2, cnt +1)
    elif a%2 == 1:
        recall(a//3, cnt+1)
    
recall(N,0)
