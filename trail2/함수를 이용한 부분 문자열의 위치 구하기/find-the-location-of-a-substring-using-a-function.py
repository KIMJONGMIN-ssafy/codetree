text = input()
pattern = input()

# Please write your code here.

def gogo(a,b):
    if a.find(b) != -1:
        return True
    return False

if gogo(text, pattern):
    print(text.find(pattern))
else:
    print(-1)

