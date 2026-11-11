n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def hap(a, b):
    total = 0

    for i in range(a-1, b):
        total += arr[i]

    return total

for a,b in queries:
    print(hap(a,b))
