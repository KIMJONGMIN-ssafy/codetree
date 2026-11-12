N = int(input())

# Please write your code here.

def go(a):
    if a ==1:
        return 1
    if a == 2:
        return 2
    
    return (go(a//3)+go(a-1))

print(go(N))