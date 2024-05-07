def power_base_sum(base, power):
    result = base**power
    sum = 0
    for i in str(result):
        sum += int(i)
    return sum
