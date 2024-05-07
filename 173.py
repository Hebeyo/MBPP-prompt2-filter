def remove_splchar(text):
    return ''.join(e for e in text if e.isalnum())
