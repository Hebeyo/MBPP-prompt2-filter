def tuple_int_str(tuple_str):
    result = []
    for x in tuple_str:
        result.append((int(x[0]), int(x[1]))    )
    return tuple(result)
