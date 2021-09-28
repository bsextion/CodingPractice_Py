
def knapsack(weights, prices, capacity):
    result = []
    solve(0, capacity, weights, prices, [], [], result)
    return result[0]



def solve(i, capacity, weights, prices, current_weight, current_price, result):
    if sum(current_weight) <= capacity and sum(current_weight) > 0:
        result.append(current_price)
        return

    if sum(current_weight) > capacity:
        return

    for j in range(i, len(weights)):
        temp_price = current_price + [prices[j]]
        temp_weight = current_weight + [weights[j]]
        if weights[j] not in current_weight and prices[j] not in current_price:
            solve(j, capacity, weights, prices, temp_weight, temp_price, result)




    return

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


print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
