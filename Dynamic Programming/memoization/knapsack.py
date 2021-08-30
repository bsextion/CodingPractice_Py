
def knapsack(weights, prices, capacity):
    return solve(0, capacity-weights[0], weights, prices)

def solve(index, capacity, weights, prices):
    if index >= len(weights) or capacity == 0:
        return 0

    temp1 = solve(index+1, capacity-weights[index+1], weights,prices) + prices[index+1]
    temp2 = solve(index+2, capacity-weights[index+1], weights,prices) + prices[index+2]
    result = max(temp1, temp2)

    return result

    # for i in enumerate(weights):
    #     temp1 = solve(i-1)
    #     temp2 = temp1 - prices[i]
    #     result = max(temp1, temp2)
    # return result

# def solve(index, capacity, weights, prices):
#     if index == 0 or capacity == 0:
#         result = 0
#     elif weights[index] > capacity:
#         result = solve(index-1, capacity, weights, prices)
#     else:
#         temp1 = solve(index-1, capacity,weights, prices)
#         temp2 = prices[index] + solve(index-1, capacity - weights[index],weights, prices)
#         result = max(temp1, temp2)
#     return result


print(knapsack([2,1,1,3], [2,8,1,10], 4))
