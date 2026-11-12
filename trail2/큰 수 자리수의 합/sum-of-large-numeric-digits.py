a, b, c = map(int, input().split())

# Please write your code here.

ans = a*b*c

def lets(a):
    if a == 0:
        return 0
    
    return (a%10) + lets(a//10)
    

print(lets(ans))

