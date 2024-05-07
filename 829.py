def second_frequent(input):
    counts = {}
    for i in input:
        if i not in counts:
            counts[i] = 0
        counts[i] += 1
    counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return counts[1][0]
