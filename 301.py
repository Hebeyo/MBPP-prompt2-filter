def dict_depth(d):
    if isinstance(d, dict):
        depth = 0
        for key in d:
            depth = max(depth, dict_depth(d[key]))
        return depth + 1
    else:
        return 0
