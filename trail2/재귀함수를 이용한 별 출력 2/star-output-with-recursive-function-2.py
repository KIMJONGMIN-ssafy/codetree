n = int(input())

# Please write your code here.

def star(n):
    
    if n == 0:
        return

    stars = ''

    for _ in range(n):
        stars += '* '
    print(stars)
    star(n-1)
    print(stars)

star(n)