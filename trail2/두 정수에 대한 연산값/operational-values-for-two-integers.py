a, b = map(int, input().split())

# Please write your code here.

def cul(a,b):
    if a<b:
        b= b+25
        a = a*2
    elif a>b:
        a= a+25
        b= b*2

    print(a,b)

cul(a,b)


    