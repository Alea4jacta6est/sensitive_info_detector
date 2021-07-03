# Sensitive information detector

The app that detects sensitive information in the text

## Install dependencies

`!python -m spacy download en_core_web_trf`

`pip install -r requirements.txt`

### How does it work?

This tool extracts:

o	Swiss City Names (extract all GPEs using spacy default model, check whether the location is from Switzerland)
o	Private Names (extract all PERSON tags)
o	Birth Dates (regexp that finds different dates)

and makes a conclusion about content sensitivity. 
If one of the mentioned entities is present in the text, the text is treated as sensitive.

Swiss cities are taken from https://simplemaps.com/data/world-cities (merged different types of writing)
