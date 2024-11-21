# Number of warehouses
n = 4

# Number of suppliers
m = 3

# Cost matrix C where C[i][j] is the cost to supply warehouse j from supplier i
C = [
    [4, 2, 5, 6],
    [7, 3, 2, 4],
    [3, 6, 1, 7]
]

# DP table to store the minimum cost up to each warehouse
dp = [[float('inf')] * n for _ in range(m)]

# Initialize the first warehouse costs
for i in range(m):
    dp[i][0] = C[i][0]

# Fill the DP table
for j in range(1, n):
    for i in range(m):
        for k in range(m):
            dp[i][j] = min(dp[i][j], dp[k][j-1] + C[i][j])

# Find the minimum cost to supply all warehouses
min_cost = float('inf')
for i in range(m):
    min_cost = min(min_cost, dp[i][n-1])

print(f"Minimum supply chain cost: {min_cost}")