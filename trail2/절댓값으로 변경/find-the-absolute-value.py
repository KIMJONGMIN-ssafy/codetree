n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def ab(a):
    for i in range(len(a)):
        a[i] = abs(a[i])

    print(*a)

ab(arr)