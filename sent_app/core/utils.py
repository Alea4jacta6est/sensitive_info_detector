import spacy
from spacy import displacy

import json
import re
import os


with open("sent_app/core/swiss_cities.json") as file:
    cities = set(json.load(file)["cities"])

birthdate_regex = "\d{2}.\w{2}.\d{4}"
nlp = spacy.load("en_core_web_trf")

def has_birthdate(text):
    result = re.findall(birthdate_regex, text)
    if result:
        return True
    return False

def classify_text_by_ents(text):
    doc = nlp(text)
    html = displacy.render(doc, style="ent")
    ents_dict = {}
    for ent in doc.ents:
        ents_dict[ent.label_] = ent.text
    # Business logic
    if "PERSON" in ents_dict:
        return "Sensitive", html
    elif "GPE" in ents_dict and set(ents_dict["GPE"]).intersection(cities):
        return "Sensitive", html
    elif has_birthdate(doc.text):
        return "Sensitive", html
    else:
        return "Not sensitive", html

def extract_text_data(root_folder_or_path="data/"):
    """Opens txt files, returns texts

    Args:
        root_folder (str, optional): root dir with data or a path to file. 
        Defaults to "data/".

    Returns:
        texts: list of strings
    """
    final_texts = []
    if ".txt" not in root_folder_or_path:
        file_samples = os.listdir(root_folder_or_path)
        for filename in file_samples:
            with open(f"{root_folder_or_path}{filename}") as file:
                sample = file.read()
                final_texts.append(sample)
        return final_texts
    else:
        with open(f"data/{root_folder_or_path}") as file:
            sample = file.read()
            return sample