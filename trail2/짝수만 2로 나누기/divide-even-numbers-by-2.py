n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def gogo(a):
    for i in range(len(a)):
        if a[i] % 2 ==0:
            a[i] = a[i]//2
    print(*a)

gogo(arr)
    