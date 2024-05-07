def sum_of_digits(nums):
    sum=0
    for i in nums:
        for j in str(i):
            if j.isdigit():
                sum+=int(j)
    return sum
