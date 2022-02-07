import spacy 

def spacylist(text):
    
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        if ent.label_ == "PERSON": 
          entities.append(ent.text)
    return entities