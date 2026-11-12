n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def lets(a,b):
    while b:
        a,b = b,a%b
    return a

def go(a,b):
    return a*b // lets(a,b)

def home(nums):
    result = nums[0]
    for num in nums:
        result = go(result, num)

    return result

print(home(arr))
