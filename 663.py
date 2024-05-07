def find_max_val(n, x, y): 
    ans = -float('inf')
    for k in range(n+1):
        if k % x == y:
            ans = max(ans, k)
    return (ans if (ans >= 0 and ans <= n) else -1)
