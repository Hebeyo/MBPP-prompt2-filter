def num_position(text):
    for i in range(len(text)):
        if text[i].isdigit():
            return i
