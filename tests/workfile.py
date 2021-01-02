import spacy

from spacy.lang.en import English

nlp = spacy.load("en_core_web_sm")

doc = nlp("76,502 METRIC TONNES")

for ent in doc.ents:
    print(ent.text, ent.label_)


