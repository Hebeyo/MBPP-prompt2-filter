def diff_even_odd(list1):
    first_even = -1
    first_odd = -1
    for i in range(len(list1)):
        if list1[i]%2==0:
            first_even = list1[i]
            break
    for i in range(len(list1)):
        if list1[i]%2!=0:
            first_odd = list1[i]
            break
    return (first_even-first_odd)
