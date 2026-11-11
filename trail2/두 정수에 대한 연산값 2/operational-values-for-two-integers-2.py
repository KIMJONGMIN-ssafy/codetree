a, b = map(int, input().split())

# Please write your code here.

def gogo(a,b):
    if a<b:
        a = a+10
        b = b*2
    elif a>b:
        a = a*2
        b = b+10
    return a,b

print(*gogo(a,b))
