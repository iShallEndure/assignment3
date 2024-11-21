def min_inventory_cost(demand, holding_cost, ordering_cost, stockout_cost, periods):
    dp = [[float('inf')] * (len(demand) + 1) for _ in range(periods + 1)]
    dp[0][0] = 0

    for i in range(1, periods + 1):
        for j in range(len(demand) + 1):
            # Holding cost
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + holding_cost[j - 1])
            # Ordering cost
            if j < len(demand):
                dp[i][j] = min(dp[i][j], dp[i - 1][0] + ordering_cost + stockout_cost[j])

    return dp[periods][len(demand)]

# Example usage:
demand = [20, 30, 40]  # Units of demand for each period
holding_cost = [1, 1.5, 2]  # Holding cost per unit for each period
ordering_cost = 50  # Fixed cost for placing an order
stockout_cost = [10, 15, 20]  # Stockout cost per unit for each period
periods = 3  # Number of periods

min_cost = min_inventory_cost(demand, holding_cost, ordering_cost, stockout_cost, periods)
print(f"The minimum inventory cost is: {min_cost}")