n = int(input())

# Please write your code here.
a1 = []
def first(n):
    global a1
    if n == 0:
        return

    first(n-1)
    a1.append(n)

a2 = []
def second(a):
    global a2
    if a == 0:
        return
    a2.append(a)
    second(a-1)


first(n)
second(n)
print(*a1)
print(*a2)

