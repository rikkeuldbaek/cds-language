#!/usr/bin/env bash

#create virtual environment
python -m venv spacy_env

#activate virtual environment
source ./spacy_env/bin/activate

#install requirements
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# run the code
python3 src/session6_ru.py

# deactivate environment
deactivate


#intall the model
python3 -m spacy download en_core_web_md


