N = int(input())

# Please write your code here.

def go(a):
    if a == 1:
        return 2
    if a == 2:
        return 4

    
    return (go(a-1)*go(a-2))%100

print(go(N))