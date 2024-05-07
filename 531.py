def min_coins(coins, m, V): 
    if (V == 0): 
        return 0
    res = float('inf')
    for i in range(0, m): 
        if (coins[i] <= V): 
            sub_res = min_coins(coins, m, V-coins[i]) 
            if (sub_res != float('inf') and sub_res + 1 < res): 
                res = sub_res + 1  
    return res
