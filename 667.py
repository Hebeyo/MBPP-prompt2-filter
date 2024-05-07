def Check_Vow(string, vowels):
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count
