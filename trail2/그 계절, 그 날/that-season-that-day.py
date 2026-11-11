Y, M, D = map(int, input().split())

# Please write your code here.

def checking(Y,M,D):
    cc = False
    yun = False
    if Y%4==0 and not Y % 100==0:
        yun = True
    if Y%4==0 and Y % 100 ==0 and Y %400 ==0:
        yun = True


    if yun:
        if M%2 == 1 and 1<=M<=7:
            if 1<=D<=31:
                cc = True
        if M%2 == 1 and 7<M<=12:
            if 1<=D<=30:
                cc = True

        if M%2 == 0 and 1<=M<=6 and not M==2:
            if 1<=D<=30:
                cc = True
        if M%2 == 0 and 6<M<=12 and not M ==2:
            if 1<=D<=31:
                cc = True
        if M==2:
            if 1<=D<=29:
                cc = True

    if not yun:
        if M%2 == 1 and 1<=M<=7:
            if 1<=D<=31:
                cc = True
        if M%2 == 1 and 7<M<=12:
            if 1<=D<=30:
                cc = True

        if M%2 == 0 and 1<=M<=6 and not M==2:
            if 1<=D<=30:
                cc = True
        if M%2 == 0 and 6<M<=12 and not M ==2:
            if 1<=D<=31:
                cc = True
        if M==2:
            if 1<=D<=28:
                cc = True
        
    if cc:
        if 3<=M<=5:
            print('Spring')
        elif 6<=M<=8:
            print('Summer')
        elif 9<=M<=11:
            print('Fall')
        elif M == 12 or 1<=M<=2:
            print('Winter')

    if not cc:
        print('-1')

checking(Y,M,D)
