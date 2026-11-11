M, D = map(int, input().split())

# Please write your code here.

def checking(a,b):
    if M % 2 == 0 and 1<=M<=6 and not M == 2:
        
        if 1<=D<=30:
            return True
    if M == 2:
        if 1<=D<=28:
            return True

    if M % 2 == 0 and 6<M<=12 and not M == 2:
        if 1<=D<=31:
            return True

    if M % 2 == 1 and 1<=M<=7:
        if 1<=D<=31:
            return True

    if M % 2 == 1 and 7<M<=12:
        if 1<=D<=30:
            return True

    return False

if checking(M,D):
    print('Yes')
else:
    print('No')

