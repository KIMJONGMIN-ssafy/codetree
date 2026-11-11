N = int(input())

# Please write your code here.

def fibo(a):
    if a == 1 or a==2:
        return 1

    return fibo(a-1) + fibo(a-2)

print(fibo(N))
    