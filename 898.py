def extract_elements(numbers, n):
    i = 0
    result = []
    while i < len(numbers):
        if numbers[i:i+n] == [numbers[i]]*n:
            result.append(numbers[i])
        i += 1
    return result
