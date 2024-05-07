def mul_even_odd(list1):
    even = -1
    odd = -1
    for i in list1:
        if i%2==0:
            even = i
            break
    for i in list1:
        if i%2!=0:
            odd = i
            break
    return even*odd
