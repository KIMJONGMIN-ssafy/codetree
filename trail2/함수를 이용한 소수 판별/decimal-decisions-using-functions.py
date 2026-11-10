a, b = map(int, input().split())

# Please write your code here.

n = list(range(2,101))
ans = []
for i in range(2,101):
    prime = True
    for j in range(2,i):
        if i%j == 0:
            prime = False
            break

    if prime:
        ans.append(i)


plus =[]
for k in range(len(ans)):
    if a<=ans[k]<=b:
        plus.append(ans[k])

print(sum(plus))