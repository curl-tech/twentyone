from spacy.lang.en import English

nlp = English()

doc = nlp("Hello World!")

for tokens in doc:
    print(tokens.text)

span = doc[1:3]
print(span)