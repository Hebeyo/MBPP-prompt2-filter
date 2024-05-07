def sum_even_odd(list1):
    first_even = -1
    first_odd = -1
    for el in list1:
        if el%2==0:
            first_even = el
            break
    for el in list1:
        if el%2!=0:
            first_odd = el
            break
    return (first_even+first_odd)
