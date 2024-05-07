def check_alphanumeric(string):
    if string[-1].isalnum():
        return 'Accept'
    else:
        return 'Discard'
