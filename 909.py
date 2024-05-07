def previous_palindrome(num):
    for i in range(num-1,0,-1):
        if str(i) == str(i)[::-1]:
            return i
    return -1
