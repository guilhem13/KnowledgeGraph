from pickle import TRUE
from unittest import result
from controller import Data , Textprocessed
from nlpmodel import nltkmodel , standfordnermodel
import json


class Pipeline(): 

    def __init__(self,arxiv_url):
        self.arxiv_url = arxiv_url
        pass
    
    def get_references(self, textprocessed): 

        nltkresult = nltkmodel.nltktreelist(textprocessed)["persons"]
        Standfordresult = standfordnermodel.get_continuous_chunks(textprocessed)["persons"]
        resultList= list(set(nltkresult) | set(Standfordresult))

        return resultList

        #TODO A voir les modèles ne marche


    def make_traitement_pipeline(self): #https://export.arxiv.org/pdf/
        arxiv_data = Data.get_set_data()
        f = open("test.json", "a")
        for i in range(len(arxiv_data)):

            processor = Textprocessed(arxiv_data[i].link[0])            
            text_processed = processor.get_data_from_pdf()
            arxiv_data[i].entities_include_in_text = processor.find_entities_in_raw_text()
            arxiv_data[i].entities_from_reference = self.get_references(text_processed)
            #TODO arxiv_data[i].subject 
            f.write(json.dumps(arxiv_data[i].__dict__))
        f.close()
        return True
#TODO faire le multi threading https://ichi.pro/fr/multithreading-en-python-et-comment-y-parvenir-28270357503503