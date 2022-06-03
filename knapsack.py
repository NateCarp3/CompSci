def knapsack(capacity, items):
    if len(items) == 0 or capacity <= 0: #basecases
        return 0
    elif items[0][0] > capacity:
        return knapsack(capacity, items[1:])
    else:
        use_it = items[0][1]+ knapsack(capacity - items[0][0], items[1:])
        lose_it = knapsack(capacity, items[1:])
        return max(use_it, lose_it)
