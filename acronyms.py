acronyms = {
    'lol': 'laugh out loud',
    'idk': "I don't know",
    'smh': "shake my head",
    'tbh': "to be honest"
}

acronyms['lol'] = "lot's of love"
acronyms['bfg'] = "BIG F*ING GUN"
del acronyms['bfg']

word = 'bfg'
definition = acronyms.get(word)

print("List:")

for acronym in acronyms:
    print(acronym)

if word in acronyms:
    print(word + " is in the list")
else:
    print(word + " is not in the list")

if definition:
    print(word, 'means', definition)
else:
    print(word, 'means', definition)



sentence = 'idk' + ' what happened ' + 'tbh'
translation = acronyms.get('idk') + ' what happened ' + acronyms.get('tbh')

print("Sentence: " + sentence)
print("Translation: " + translation)