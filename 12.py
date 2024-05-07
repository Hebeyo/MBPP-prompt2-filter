def sort_matrix(M):
    result = []
    for i in range(len(M)):
        result.append(sum(M[i]))
    result = [x for _, x in sorted(zip(result, M))]
    return result
