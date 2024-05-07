def count_char_position(str1):
    count_chars = 0
    for i in range(len(str1)):
        if i == ord(str1[i].upper()) - ord('A'):
            count_chars += 1
    return count_chars
