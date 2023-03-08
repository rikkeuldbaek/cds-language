#load packages
import spacy #note we can neva eva know if the reader of this script
# has the same packages installed/loaded
#enter VIRTUAL ENVIRONMENT!!!! 



#initialize spacy
nlp = spacy.load("en_core_web_md")

text = "This is a string"
doc = nlp(text)

#create main function
def main():
    for token in text:
        print(token.text)


#run main function
if __name__ == "__main__":
    (main)





### create environment
#1)  python3 -m venv spacy_env (where spacy_env is the name of environment)
# inside spacy_env we have a lot of folders
### activate environment
#2)  source ./spacy_env/bin/activate
### install package spacy in the spacy_env
#3) pip install --upgrade pip
#3.1) pip install spacy
### running this script (will not work, since we lack to load the model in the spacy_env)
#4)  python src/session6_ru.py
### download model
# 5)python -m spacy download en_core_web_md
### running script again
# 6)python src/session6_ru.py (now works)
### deactivate environment
# 7) deactivate 

##### Note when you make a virtual environment, it takes up a lot of space
# so dont push it to github and add it to gitignore. 
#when you make a repo on github and add a gitignore (python), it automatically
# git ignores the virtual environment

###this is important bc: the user only needs python 3 installed to run this :)
### wuhu reproducibility















