def same_order(l1, l2):
    common_elements = []
    for e1 in l1:
        if e1 in l2:
            common_elements.append(e1)
    return common_elements==[e for e in l2 if e in common_elements]
