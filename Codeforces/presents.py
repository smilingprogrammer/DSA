n = int(input().strip())
arr = list(map(int, input().split()))

ans = n * [0]

for i in range(n):
    ans[arr[i] - 1] = i + 1

print(" ".join(map(str, ans)))