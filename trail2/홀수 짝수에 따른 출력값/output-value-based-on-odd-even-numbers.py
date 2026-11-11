N = int(input())

# Please write your code here.

def recall(a):
    if a <= 0:
        return 0

    return a+recall(a-2)

print(recall(N))