def roman_to_int(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    n = len(s)
    if n==1:
        return roman[s]
    res = 0
    for i in range(n-1):
        if roman[s[i]] < roman[s[i+1]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]
    return res+roman[s[-1]]
