A = input()

# Please write your code here.

def palindrome(a):
    if a == a[::-1]:
        return True
    else:
        return False

if palindrome(A):
    print('Yes')
if not palindrome(A):
    print('No')