def replace_max_specialchar(text,n):
    text = list(text)
    count = 0
    for i in range(len(text)):
        if text[i] in [' ',',','.']:
            text[i] = ':'
            count += 1
        if count == n:
            break
    return ''.join(text)
