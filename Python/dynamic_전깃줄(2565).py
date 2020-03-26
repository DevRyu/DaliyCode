N = int(input())
line = [list(map(int, input().split())) for _ in range(N)]
line = sorted(line, key = lambda x : x[0])

dp = [0] * N
dp[0] = 1

for i in range(1, N):
    min_value = 0
    for j in range(i):
        if(line[i][1] > line[j][1]):
            min_value = max(dp[j], min_value)
    dp[i] = min_value + 1
print(N - max(dp))
