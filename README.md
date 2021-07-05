# Sensitive information detector

The demo app that detects sensitive information in the text

## How to run it?

1) Locally (inside your env)

`pip install -r requirements.txt`

`python -m spacy download en_core_web_trf`

`streamlit run app.py`

2) Using docker

`docker build . -t "detector:v1"`

`docker run -p 4200:4200 "detector:v1"`

By default you can access the app here: http://localhost:4200/

### How does it work?

This tool extracts:

o	Swiss City Names (first all GPEs using spacy default model, then checks whether the location is from Switzerland)
o	Private Names (extract all PERSON tags)
o	Birth Dates (regexp that finds different dates)

and makes a conclusion about content sensitivity. 
If one of the mentioned entities is present in the text, the text is treated as sensitive. (However, if only Swiss City names are present in the text, it won't be marked as sensitive)

### What can be improved in the current approach?

0) Adding DOB tag to the user interface for a demo

1) Adding more Swiss locations and variations of their writing

2) Training a custom model for 3 tags mentioned above (with artifical data, no manual annotation needed)

3) Improving a regex for DOB extraction (if staying with rules for DOB extraction)

Swiss cities are taken from https://simplemaps.com/data/world-cities (merged different types of writing)
