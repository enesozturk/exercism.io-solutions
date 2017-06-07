def distance(string,string2):
    if len(string) == len(string2):
        return len(list(filter(lambda xy: xy[0] != xy[1], zip(string, string2))))
    else:
        raise ValueError()

