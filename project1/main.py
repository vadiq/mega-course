import json

data = json.load(open('files/data.json'))


def get_term(term):
    if term in data:
        return data[term]
    else:
        return 'no such term'


words = input('Enter term: ')


print(get_term(words))
