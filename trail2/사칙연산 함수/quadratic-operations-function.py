a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.

ans = 0

def plus(a,b):
    global ans
    ans = a + b

def minus(a,b):
    global ans
    ans = a-b

def mul(a,b):
    global ans
    ans = a*b

def divide(a,b):
    global ans
    ans = a//b

if o == '+':
    plus(a,c)
    print(f'{a} {o} {c} = {ans}')
elif o == '-':
    minus(a,c)
    print(f'{a} {o} {c} = {ans}')
    
elif o == '*':
    mul(a,c)
    print(f'{a} {o} {c} = {ans}')

elif o == '/':
    divide(a,c)
    print(f'{a} {o} {c} = {ans}')

else:
    print('False')
