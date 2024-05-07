def filter_evennumbers(nums):
    even_nums=[]
    for i in nums:
        if i%2==0:
            even_nums.append(i)
    return even_nums
