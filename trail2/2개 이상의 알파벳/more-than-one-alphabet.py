A = input()

# Please write your code here.

def gogo(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] != a[j]:
                return True


    return False

if gogo(A):
    print('Yes')
if not gogo(A):
    print('No')

