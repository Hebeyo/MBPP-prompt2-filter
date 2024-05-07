def dog_age(h_age):
    if h_age <= 0:
        return 0
    elif h_age <= 2:
        return h_age * 10.5
    else:
        return 21 + (h_age - 2) * 4
