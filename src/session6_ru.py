#load packages
import spacy #note we can neva eva know if the reader of this script
# has the same packages installed/loaded
#enter VIRTUAL ENVIRONMENT!!!! 



#initialize spacy
nlp = spacy.load("en_core_web_md")

text = "This is a string"
doc = nlp(text)

def main():
    for token in text:
        print(token.text)



if __name__ == "__main__":
    (main)