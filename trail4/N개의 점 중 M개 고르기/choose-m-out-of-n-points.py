n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

answer = float('inf')
selected = []

def dfs(start):
    global answer

    if len(selected) == m:

        max_dist = 0

        for i in range(m):
            for j in range(i + 1, m):

                x1, y1 = selected[i]
                x2, y2 = selected[j]

                dist = (x1 - x2)**2 + (y1 - y2)**2

                max_dist = max(max_dist, dist)

        answer = min(answer, max_dist)
        return

    for i in range(start, n):
        selected.append(points[i])

        dfs(i + 1)

        selected.pop()


dfs(0)

print(answer)