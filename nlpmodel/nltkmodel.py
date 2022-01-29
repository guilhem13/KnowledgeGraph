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

    results = {}
    results['persons']=persons

    
    return results