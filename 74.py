def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False
    dict = {}
    for i in range(len(colors)):
        if patterns[i] not in dict:
            dict[patterns[i]] = colors[i]
        elif dict[patterns[i]] != colors[i]:
            return False
    return True
