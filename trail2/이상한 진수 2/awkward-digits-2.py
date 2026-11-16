a = input()

max_ans = 0

for i in range(len(a)):
    arr = list(a)

    if arr[i] == '1':
        arr[i] = '0'
    else:
        arr[i] = '1'

    num = int(''.join(arr), 2)

    if max_ans < num:
        max_ans = num

print(max_ans)