y = int(input())

# Please write your code here.

ans = True

if y % 4 == 0:
    ans = True
else:
    ans = False
if y % 100 ==0 and y%400 != 0 :
    ans = False


if ans is True:
    print('true')
else:
    print('false')
