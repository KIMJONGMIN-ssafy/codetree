n = int(input())

# Please write your code here.

stars = ''

def star(a):
    global stars

    if a == 0:
        return
    
    stars += ('*')
    print(stars)

    star(a-1)

star(n)