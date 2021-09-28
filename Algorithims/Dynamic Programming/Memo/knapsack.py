def solve_knapsack(profits, weights, capacity):
  return knapsack_recursive(profits, weights, capacity, 0)

def knapsack_recursive(profits, weight, capacity, index):

    if capacity <= 0 or index >= len(weight):
        return 0

    profit1 = 0
    if weight[index] <= capacity: #is weight at index1 greater than capacitu
        profit1 = profits[index] + knapsack_recursive(profits, weight, capacity - weight[index], index+1)

    profit2 = knapsack_recursive(profits, weight, capacity, index+1) #ignore the weight/price at this index

    return max(profit1, profit2) #compare the branch







print(solve_knapsack([1, 6], [1, 2], 7))