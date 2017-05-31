def is_pangram(string):
    new_string = set([c.lower() for c in string if c.isalpha()])
    if len(new_string) >= 26: return True