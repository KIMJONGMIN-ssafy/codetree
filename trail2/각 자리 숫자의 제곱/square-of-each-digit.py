N = int(input())

# Please write your code here.

def recall(a):
    if a == 0:
        return 0
    return (a%10)**2 + recall(a//10)

print(recall(N))