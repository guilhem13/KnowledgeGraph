from nltk.tag import StanfordNERTagger, StanfordPOSTagger
PATH_TO_JAR='./rawnlpmodel/stanford-ner.jar'
PATH_TO_MODEL = './rawnlpmodel/english.muc.7class.distsim.crf.ser.gz'
stner = StanfordNERTagger(PATH_TO_MODEL,PATH_TO_JAR,encoding='utf-8')

def get_continuous_chunks(string):
    string = string
    continuous_chunk = []
    current_chunk = []

    for token, tag in stner.tag(string.split()):
        if tag != "O":
            current_chunk.append((token, tag))
        else:
            if current_chunk: # if the current chunk is not empty
                continuous_chunk.append(current_chunk)
                current_chunk = []
    # Flush the final current_chunk into the continuous_chunk, if any.
    if current_chunk:
        continuous_chunk.append(current_chunk)
    named_entities = continuous_chunk
    named_entities_str = [" ".join([token for token, tag in ne]) for ne in named_entities]
    named_entities_str_tag = [(" ".join([token for token, tag in ne]), ne[0][1]) for ne in named_entities]
    persons = []
    for l in [l.split(",") for l,m in named_entities_str_tag if m == "PERSON"]:
        for m in l:
            for n in m.strip().split(","):
                if len(n)>0:
                    persons.append(n.strip("*"))
    organizations = []
    for l in [l.split(",") for l,m in named_entities_str_tag if m == "ORGANIZATION"]:
        for m in l:
            for n in m.strip().split(","):
                n.strip("*")
                if len(n)>0:
                    organizations.append(n.strip("*"))
    locations = []
    for l in [l.split(",") for l,m in named_entities_str_tag if m == "LOCATION"]:
        for m in l:
            for n in m.strip().split(","):
                if len(n)>0:
                    locations.append(n.strip("*"))
    dates = []
    for l in [l.split(",") for l,m in named_entities_str_tag if m == "DATE"]:
        for m in l:
            for n in m.strip().split(","):
                if len(n)>0:
                    dates.append(n.strip("*"))
    money = []
    for l in [l.split(",") for l,m in named_entities_str_tag if m == "MONEY"]:
        for m in l:
            for n in m.strip().split(","):
                if len(n)>0:
                    money.append(n.strip("*"))
    time = []
    for l in [l.split(",") for l,m in named_entities_str_tag if m == "TIME"]:
        for m in l:
            for n in m.strip().split(","):
                if len(n)>0:
                    money.append(n.strip("*"))
                    
    percent = []
    for l in [l.split(",") for l,m in named_entities_str_tag if m == "PERCENT"]:
        for m in l:
            for n in m.strip().split(","):
                if len(n)>0:
                    money.append(n.strip("*"))

    entities={}
    entities['persons']= persons
    entities['organizations']= organizations
    entities['locations']= locations
    #entities['dates']= dates
    #entities['money']= money
    #entities['time']= time
    #entities['percent']= percent
    
    return entities