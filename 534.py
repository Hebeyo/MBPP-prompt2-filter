def search_literal(pattern,text):
    start = text.find(pattern)
    end = start + len(pattern)
    return (start, end)
