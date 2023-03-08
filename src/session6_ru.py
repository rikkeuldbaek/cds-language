#load packages
import spacy

#initialize spacy
nlp = spacy.load("en_core_web_lg")

text = "This is a string"
doc = nlp.(text)


for token in text:
    print(token.text)
