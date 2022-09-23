import json
from difflib import get_close_matches
data = json.load(open("2.1 data.json.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead? " % get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == 'N':
            return 'The word doesn"t exist. Please try again later'
        else:
            return 'Dont understand'
    else:
        return 'The word doesn"t exist. Please try again later'

word = input("Enter word : ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)