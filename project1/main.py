import json
from difflib import get_close_matches

data = json.load(open('files/data.json'))


def get_term(term):
    term = term.lower()
    if term in data:
        return data[term]
    elif len(get_close_matches(term, data.keys(), cutoff=0.6)) > 0:
        return recommend(term)
    else:
        return 'no such term in the dictionary'


def recommend(typo):
    # recommends a term if a typo
    term = get_close_matches(typo, data.keys(), cutoff=0.6)[0]
    todo = input(f'Did you mean "{term}"?\nY/N:\t').lower()
    if todo == 'y':
        return data[term]
    else:
        return 'sorry, pls try another term'


phrase = input('Welcome to simple explanatory dictionary, containing 49537 terms!\n'
               'Please, enter term to search:\t')
n = 1
output = get_term(phrase)
if isinstance(output, list):
    for item in output:
        print(f'{n}) {item}')
        n += 1
else:
    print(output)
