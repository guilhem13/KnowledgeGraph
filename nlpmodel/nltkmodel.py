import nltk 
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#TODO ici faudra bien mettre les nltk.dowloads car ça va s'ajouter à chaque fois. Du moins pour chaque instance 

def nltktreelist(text):
    from operator import itemgetter
    
    text = text    
    
    persons = []
    #organizations = []
    #locations =[]
    #genpurp = []

    for l in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text))):
        if isinstance(l,nltk.tree.Tree):
            if l.label() == 'PERSON':
                if len(l)== 1:
                    if l[0][0] in persons:
                        pass
                    else:
                        persons.append(l[0][0])
                else:
                    if " ".join(map(itemgetter(0), l)) in persons:
                        pass
                    else:
                        persons.append(" ".join(map(itemgetter(0), l)).strip("*"))
   
    """
    for o in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text))):
        if isinstance(o,nltk.tree.Tree):
            if o.label() == 'ORGANIZATION':
                if len(o)== 1:
                    if o[0][0] in organizations:
                        pass
                    else:
                        organizations.append(o[0][0])
                else:
                    if " ".join(map(itemgetter(0), o)) in organizations:
                        pass
                    else:
                        organizations.append(" ".join(map(itemgetter(0), o)).strip("*"))
    

    for o in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text))):
        if isinstance(o,nltk.tree.Tree):
            if o.label() == 'LOCATION':
                if len(o)== 1:
                    if o[0][0] in locations:
                        pass
                    else:
                        locations.append(o[0][0])
                else:
                    if " ".join(map(itemgetter(0), o)) in locations:
                        pass
                    else:
                        locations.append(" ".join(map(itemgetter(0), o)).strip("*"))
    
    for e in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(text))):
        if isinstance(o,nltk.tree.Tree):
            if o.label() == 'GPE':
                if len(o)== 1:
                    if o[0][0] in genpurp:
                        pass
                    else:
                        genpurp.append(o[0][0])
                else:
                    if " ".join(map(itemgetter(0), o)) in genpurp:
                        pass
                    else:
                        genpurp.append(" ".join(map(itemgetter(0), o)).strip("*"))
                        
       
    """

    results = {}
    results['persons']=persons
    #results['organizations']=organizations
    #results['locations']=locations
    #results['genpurp'] = genpurp
    
    return results