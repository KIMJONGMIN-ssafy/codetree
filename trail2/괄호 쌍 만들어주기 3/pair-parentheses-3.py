s = input()

open_cnt = 0
ans = 0

for ch in s:
    if ch == '(':
        open_cnt += 1
    else:
        ans += open_cnt

print(ans)