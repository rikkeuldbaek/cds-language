#!/usr/bin/env bash
python3.9 -m pip install -r requirements.txt
python3 -m spacy download en_core_web_md

git config --global user.email "rikke_uldbaek@hotmail.com"
git config --global user.name "rikkeuldbaek"