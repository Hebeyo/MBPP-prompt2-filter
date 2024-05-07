def remove_empty(tuple1): #L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
    return [t for t in tuple1 if t]
