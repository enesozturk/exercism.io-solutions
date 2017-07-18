import re
from collections import Counter
def word_count(string):
    dizi = re.split(r'[;:!!&@$%^&,.\s]\s*', string)
    array = dict(Counter(dizi))
    return(array)