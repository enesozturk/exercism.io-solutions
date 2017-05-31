def to_rna(string):
    string = [l.upper() for l in string]
    new_string = []
    for i in string: 
        if i=='G': new_string.append('C')
        elif i=='C': new_string.append('G')
        elif i=='T': new_string.append('A')
        elif i=='A': new_string.append('U')
        elif i=='U': new_string.clear()
        else: 
            new_string.clear() 
            break
    new_string = ''.join(new_string)
    return new_string
